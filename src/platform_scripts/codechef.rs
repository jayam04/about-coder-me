pub fn get_contest_rating(username: &str) -> String {
    let url = format!("https://www.codechef.com/users/{}", username);
    let response = reqwest::blocking::get(url).unwrap();
    let html_content = response.text().unwrap();

    // parse HTML, scrape rating, etc

    let document = scraper::Html::parse_document(&html_content);
    let mut product_name = "hehe".to_string();
    let html_product_selector = scraper::Selector::parse(".rating-number").unwrap();
    let html_products = document.select(&html_product_selector);
    for html_product in html_products {
        product_name = html_product.inner_html();
        // remove everything from < in product_name
        product_name = product_name.split("<").collect::<Vec<&str>>()[0].to_string();

        // remove ? in codechef rating
        product_name = product_name.split("?").collect::<Vec<&str>>()[0].to_string();

        // return product name
        println!("{product_name}");
    }
    product_name
}