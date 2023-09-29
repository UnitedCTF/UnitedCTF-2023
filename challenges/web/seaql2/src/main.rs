use actix_web::{
    get,
    web::{self, Data},
    App, HttpResponse, HttpServer,
};
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
async fn index(
    tmpl: web::Data<Handlebars<'_>>,
    pool: web::Data<SqlitePool>,
    query: web::Query<Info>,
) -> HttpResponse {
    let sql_query = match &query.title {
        Some(t) if t.trim().is_empty() => "SELECT * FROM books WHERE title".to_string(),
        Some(t) => format!("SELECT * FROM books WHERE title LIKE '%{}%'", t),
        None => "SELECT * FROM books".to_string(),
    };

    let optional_title = query.title.clone().unwrap_or("".into());

    let restricted_keywords: Vec<&str> = vec![
        "hidden_secrets",
        "sqlite",
        "sql",
        "table",
        "FROM",
        "UNION",
        "SELECT",
        "WHERE",
        "FROM",
    ];

    if restricted_keywords
        .iter()
        .any(|&keyword| optional_title.contains(keyword))
    {
        let mut data = serde_json::Map::new();
        data.insert(
            "default_search".to_string(),
            serde_json::Value::from(query.title.clone().unwrap_or("".to_string())),
        );
        data.insert(
            "error".to_string(),
            "Nice try! But that's not the right way.".into(),
        );
        let body = tmpl.render("index", &data).unwrap();
        return HttpResponse::Forbidden().body(body);
    }

    let rows: Vec<(i32, String, String)> = sqlx::query_as(&sql_query)
        .fetch_all(&**pool)
        .await
        .unwrap_or_else(|_| vec![(0, "Not Found".to_string(), "Unknown".to_string())]);

    let book_titles: Vec<serde_json::Value> = rows
        .into_iter()
        .map(|(_, title, _)| serde_json::Value::from(title))
        .collect();

    let mut data = serde_json::Map::new();
    data.insert("books".to_string(), serde_json::Value::Array(book_titles));
    data.insert(
        "default_search".to_string(),
        serde_json::Value::from(query.title.clone().unwrap_or("".to_string())),
    );

    let body = tmpl.render("index", &data).unwrap();
    HttpResponse::Ok().body(body)
}

#[get("/details/{title}")]
async fn details(
    tmpl: web::Data<Handlebars<'_>>,
    pool: web::Data<SqlitePool>,
    title: web::Path<String>,
) -> HttpResponse {
    let title = &*title;

    tracing::info!("{:?}", title);
    let sql_query = "SELECT * FROM books WHERE title = ?";

    let row: (i32, String, String) = sqlx::query_as(&sql_query)
        .bind(title)
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

    handlebars
        .register_template_string("index", include_str!("./index.hbs"))
        .unwrap();
    handlebars
        .register_template_string("details", include_str!("./details.hbs"))
        .unwrap();

    // Ensure the table exists and has a unique constraint on the title.
    sqlx::query(
        r#"
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            review TEXT
        );
        CREATE TABLE IF NOT EXISTS hidden_secrets (
            secret TEXT
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
    ('Pirate Legends', 'Stories and myths from the golden age of piracy.');
    INSERT OR IGNORE INTO hidden_secrets (secret) VALUES
        ('flag-P1r4t3s_Ar3nt_Th3_0nly_0n3s_Wh0_L0v3_G0ld!');
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

