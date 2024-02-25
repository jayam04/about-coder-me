#[macro_use] extern crate rocket;
use rocket::tokio;
use tokio::task;
mod platform_scripts;
use platform_scripts::codechef::get_contest_rating;

#[get("/world")]
fn world() -> &'static str {
    "Hello, world!"
}

#[get("/")]
fn ss() -> &'static str {
    "ss, world!"
}

#[get("/codechef/<username>")]
async fn get_codechef_data(username: &str) -> String {

    let rating = task::block_in_place(|| {
        // Call blocking code here
        get_contest_rating(username) 
    });

    rating
}

#[rocket::main]
async fn main() -> Result<(), rocket::Error> {
    let _rocket = rocket::build()
    .mount("/", routes![world])
    .mount("/", routes![ss])

    .mount("/", routes![get_codechef_data])

    .launch()
    .await?;

    Ok(())
}