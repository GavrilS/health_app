const newArticleForm = document.getElementById('create-article');
const createArticleBtn = document.getElementById('new-article');

createArticleBtn.addEventListener('click', () => {
    newArticleForm.style.display = 'block';
});

function getUrlPath() {
    let path = window.location.pathname;
    if (path.startsWith("/")) {
        path = path.substring(1);
    }
    let pathArray = path.split("/");
    return pathArray;
}

function createUrlPath() {
    let pathArray = getUrlPath()
    pathArray.forEach(item => {
        
    })
}