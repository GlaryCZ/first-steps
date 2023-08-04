use std::fs;
use std::io;
use std::io::Write;

fn print(s: &str) {
    io::stdout().flush().unwrap();
    print!("{}", s);
    io::stdout().flush().unwrap();
}

fn input(message: &str) -> String {
    print(message);
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let i: &str = input.trim();
    return i.to_string();
}

fn main() {
    let mut run: bool = true;
    while run {
        print(">>");
        let input: String = input("");
        let split = input.split(" ");
        let vec: Vec<&str> = split.collect();
        if input == "exit" {
            println!("program exiting...");
            run = false;
        } else if input == "" {
        } else if input == "help" {
            print("list of commands:\n    echo 'something'\n    cat 'filepath'");
        } else if vec[0] == "ls" {
            let mut pp = "./";
            if vec[1].len() == 0 {
                pp = vec[1];
            }
            let paths = fs::read_dir(pp).unwrap();
            for path in paths {
                println!("{}", path.unwrap().path().display());
            }
        } else if vec[0] == "echo" {
            println!("{}", vec[1]);
        } else if vec[0] == "cat" {
            let file_content = std::fs::read_to_string(vec[1]).expect("could not open file");
            println!("{}", file_content);
        } else {
            println!("invalid input");
        }
    }
}
