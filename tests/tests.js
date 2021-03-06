module.exports = {
    'global'(browser) {
    browser.url("http://localhost:5000/global")
    .assert.elementPresent(".card-text");
    },
    'usa'(browser) {
    browser.url("http://localhost:5000/usa")
    .assert.elementPresent(".card-text");
    },
    'canada'(browser) {
    browser.url("http://localhost:5000/canada")
    .assert.elementPresent(".card-text");
    },
    'mexico'(browser) {
    browser.url("http://localhost:5000/mexico")
    .assert.elementPresent(".card-text");
    },
    'globalCanPaginate'(browser) {
    browser.url("http://localhost:5000/usa?limit=20")
    .assert.elementPresent(".card-text");
    },



}