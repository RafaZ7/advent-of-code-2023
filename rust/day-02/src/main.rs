use regex::Regex;
use std::cmp;

fn extract_number_with_pattern(input: &str, pattern: &Regex) -> i32 {
    // Try to find a match in the input string
    if let Some(capture) = pattern.captures(input) {
        // Extract the captured number and convert it to an integer
        if let Some(number_str) = capture.get(1) {
            return number_str.as_str().parse().unwrap_or(0);
        }
    }

    0
}

#[derive(Debug)]
struct CubeSet {
    blue: i32,
    green: i32,
    red: i32,
}

impl CubeSet {
    fn new(blue: i32, green: i32, red: i32) -> Self {
        Self {
            blue: blue,
            green: green,
            red: red,
        }
    }

    fn from_string(input: &str) -> Self {
        let red_pattern = Regex::new(r"(\d+) red").expect("Invalid regex");
        let blue_pattern = Regex::new(r"(\d+) blue").expect("Invalid regex");
        let green_pattern = Regex::new(r"(\d+) green").expect("Invalid regex");

        let red_value = extract_number_with_pattern(input, &red_pattern);
        let blue_value = extract_number_with_pattern(input, &blue_pattern);
        let green_value = extract_number_with_pattern(input, &green_pattern);

        return Self::new(blue_value, green_value, red_value);
    }

    fn is_valid(&self, other: &CubeSet) -> bool {
        self.blue <= other.blue && self.green <= other.green && self.red <= other.red
    }

    fn power(&self) -> i32 {
        self.blue * self.green * self.red
    }
}

#[derive(Debug)]
struct Game {
    n: i32,
    cube_set: Vec<CubeSet>,
}

impl Game {
    fn new(n: i32, cube_set: Vec<CubeSet>) -> Self {
        Self {
            n: n,
            cube_set: cube_set,
        }
    }

    fn is_valid(&self, cube_set: &CubeSet) -> bool {
        self.cube_set
            .iter()
            .all(|game_cube_set| game_cube_set.is_valid(cube_set))
    }

    fn from_string(string: &str) -> Game {
        let parts: Vec<&str> = string.split(":").collect();
        let n = parts[0]
            .trim()
            .split_whitespace()
            .nth(1)
            .unwrap()
            .parse()
            .unwrap();
        let cube_set_string = parts[1].trim();
        let cube_set: Vec<CubeSet> = cube_set_string
            .split(';')
            .map(|cube_set| CubeSet::from_string(cube_set))
            .collect();

        Game { n, cube_set }
    }

    fn minimum_set(&self) -> CubeSet {
        let blue = self
            .cube_set
            .iter()
            .map(|cube_set| cube_set.blue)
            .fold(i32::MIN, cmp::max);
        let green = self
            .cube_set
            .iter()
            .map(|cube_set| cube_set.green)
            .fold(i32::MIN, cmp::max);
        let red = self
            .cube_set
            .iter()
            .map(|cube_set| cube_set.red)
            .fold(i32::MIN, cmp::max);

        CubeSet { blue, green, red }
    }
}

fn game_solver_1(games_string: &str, max_set: &CubeSet) -> i32 {
    let games: Vec<Game> = games_string
        .trim()
        .lines()
        .map(|game_string| Game::from_string(game_string))
        .collect();

    games
        .iter()
        .filter(|game| game.is_valid(max_set))
        .map(|game| game.n)
        .sum()
}

fn game_solver_2(games_string: &str) -> i32 {
    let games: Vec<Game> = games_string
        .trim()
        .lines()
        .map(|game_string| Game::from_string(game_string))
        .collect();

    games.iter().map(|game| game.minimum_set().power()).sum()
}

fn main() {
    let input = include_str!("../../../data/day2.txt");

    let game_1_result = game_solver_1(input, &CubeSet::from_string("12 red, 14 blue, 13 green"));
    println!("game_1_result: {}", game_1_result);

    let game_2_result = game_solver_2(input);
    println!("game_2_result: {}", game_2_result);
}
