# --- Build Stage ---

FROM rust:1.68 as builder

WORKDIR /usr/src/app

COPY Cargo.toml ./

COPY ./src/ ./src/
RUN cargo build --release

# --- Production Stage ---

FROM debian:bullseye-slim as runtime

WORKDIR /app
RUN touch /app/db.sqlite
RUN apt-get update -y \
        && apt-get install -y --no-install-recommends openssl ca-certificates \
        && apt-get autoremove -y \
            && apt-get clean -y \
            && rm -rf /var/lib/apt/lists/*



COPY --from=builder /usr/src/app/target/release/seaql .


EXPOSE 8080

# Command to run the binary
ENTRYPOINT ["./seaql"]
