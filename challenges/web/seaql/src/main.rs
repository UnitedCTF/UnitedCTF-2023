use actix_web::{web::{self, Data}, HttpResponse, HttpServer, App, get};
use handlebars::Handlebars;
use serde::Deserialize;
use sqlx::SqlitePool;

pub struct Book {
    pub id: u32,
    pub title: String,
    pub author: String,
    pub rating: u8,
    pub review: String,
}

#[derive(Deserialize, Clone)]
struct Info {
    title: Option<String>,
}

#[get("/")]
async fn index(tmpl: web::Data<Handlebars<'_>>, pool: web::Data<SqlitePool>, query: web::Query<Info>) -> HttpResponse {
    let title = &query.title;

    let sql_query = match title {
        Some(t) if t.trim().is_empty() => "SELECT * FROM books WHERE title not in ('Flag of Sea')".to_string(),
        Some(t) => format!("SELECT * FROM books WHERE title LIKE '%{}%' and title not in ('Flag of Sea')", t),
        None => "SELECT * FROM books WHERE title not in ('Flag of Sea')".to_string(),
    };

    let rows: Vec<(i32, String, String)> = sqlx::query_as(&sql_query)
        .fetch_all(&**pool)
        .await
        .unwrap_or_else(|_| vec![(0, "Not Found".to_string(), "Unknown".to_string())]);

    let book_titles: Vec<serde_json::Value> = rows.into_iter()
        .map(|(_, title, _)| serde_json::Value::from(title))
        .collect();

    let mut data = serde_json::Map::new();
    data.insert("books".to_string(), serde_json::Value::Array(book_titles));
    data.insert("default_search".to_string(), serde_json::Value::from(query.title.clone().unwrap_or("".to_string())));

    let body = tmpl.render("index", &data).unwrap();
    HttpResponse::Ok().body(body)
}

#[get("/details/{title}")]
async fn details(tmpl: web::Data<Handlebars<'_>>, pool: web::Data<SqlitePool>, title: web::Path<String>) -> HttpResponse {

    let title = &*title;

    tracing::info!("{:?}", title);
    let sql_query = format!(r#"SELECT * FROM books WHERE title = "{}""#, title);


    let row: (i32, String, String) = sqlx::query_as(&sql_query)
        .fetch_one(&**pool)
        .await
        .unwrap_or((0, "Not Found".to_string(), "Unknown".to_string()));

    tracing::info!("{:?}", row);

    let mut data = serde_json::Map::new();
    data.insert("title".to_string(), serde_json::Value::from(row.1));
    data.insert("description".to_string(), serde_json::Value::from(row.2));

    let body = tmpl.render("details", &data).unwrap();
    HttpResponse::Ok().body(body)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "debug");
    env_logger::init();
    let pool = SqlitePool::connect("sqlite:db.sqlite?mode=ro").await.unwrap();
    let write_pool = SqlitePool::connect("sqlite:db.sqlite").await.unwrap();
    let mut handlebars = Handlebars::new();

    handlebars.register_template_string("index", include_str!("./index.hbs")).unwrap();
    handlebars.register_template_string("details", include_str!("./details.hbs")).unwrap();

     // Ensure the table exists and has a unique constraint on the title.
    sqlx::query(
        r#"
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            review TEXT
        );
        "#,
    )
    .execute(&write_pool)
    .await
    .unwrap();

    // Insert default entries, but only if they don't already exist.
    sqlx::query(
        r#"
    INSERT OR IGNORE INTO books (title, review)
    VALUES
    ('The Pirate Queen', 'A tale of the legendary female pirate ruler of the Seven Seas.'),
    ('Blackbeard''s Last Stand', 'Unraveling the mystery of the most feared pirate of all time.'),
    ('Treasures of the Ghost Ship', 'A young sailor discovers a ghost ship filled with treasures and dark secrets.'),
    ('Skull Island', 'An expedition to an uncharted island reveals a land still ruled by pirates.'),
    ('The Buccaneer''s Code', 'The unwritten rules that govern the world of piracy.'),
    ('The Parrot''s Tale', 'A light-hearted adventure seen through the eyes of a pirate captain''s parrot.'),
    ('Flag of Sea', 'flag-sQ3Al1t3I73ct10n_h3f2ff - The story behind the most notorious pirate flag ever raised.'),
    ('Pirate Legends', 'Stories and myths from the golden age of piracy.');
    "#,
    )
    .execute(&write_pool)
    .await
    .unwrap();

    drop(write_pool);

    HttpServer::new(move || {
        App::new()
            .app_data(Data::new(pool.clone()))
            .app_data(Data::new(handlebars.clone()))
            .service(index)
            .service(details)
    })
        .bind("0.0.0.0:8080")?
        .run()
    .await
}
