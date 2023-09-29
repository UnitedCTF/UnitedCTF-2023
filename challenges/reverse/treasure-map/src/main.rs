use std::io;

fn encode(s: &str) -> Vec<u8> {
    s.bytes().map(|b| b.reverse_bits()).collect()
}

fn generate_flag(location: &str) -> String {
    format!("flag-{}", hex::encode(location))
}

fn main() {
    let secret_passphrase = encode("CaptainCrunch");
    let secret_location = "10.1234,-50.1234";

    println!("Enter the secret passphrase:");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input_trimmed = input.trim();

    if encode(input_trimmed) == secret_passphrase {
        println!("{}", generate_flag(secret_location));
    } else {
        println!("Wrong passphrase, no treasure for ye!");
        println!("Here's your encoded value: {}", hex::encode(encode(input_trimmed)));
    }
}
