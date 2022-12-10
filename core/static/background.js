function set_background() {
    var wallpapers = ["https://images.designtrends.com/wp-content/uploads/2015/12/10063828/Space-Backgrounds11.jpg",
    "https://images.designtrends.com/wp-content/uploads/2015/12/10062723/Space-Backgrounds5.jpg",
    "https://images.designtrends.com/wp-content/uploads/2015/12/10064325/Space-Backgrounds14.jpg",
    "https://images.designtrends.com/wp-content/uploads/2015/12/10065032/Space-Backgrounds17.jpg",
    "https://wallpaperheart.com/wp-content/uploads/2018/04/real-space-wallpapers9.jpg",
    ];
    var query = wallpapers[Math.floor(Math.random() * wallpapers.length)];
    document.body.style.backgroundImage = "url(" + query + ")";
}