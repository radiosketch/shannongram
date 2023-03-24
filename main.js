/**
 * main.js
 * 
 * by rad1osketxh
 */
import {quotes} from './movie_quotes.js'
import {urls} from './image_urls.js'

/**
 * Setting up creation of posts
 */
var feed = document.getElementById('feed');
console.log(feed);
var post = document.getElementById('post');
console.log(post.childNodes[3])


/**
 * Infinite Scrolling, thanks to:
 * https://webdesign.tutsplus.com/tutorials/how-to-implement-infinite-scrolling-with-javascript--cms-37055
 */
const cardIncrease = 10;
const cardLimit = 99;
const pageCount = Math.ceil(cardLimit / cardIncrease);
let currentPage = 1;

const getRandomColor = () => {
    const h = Math.floor(Math.random() * 360);

    return `hsl(${h}deg, 90%, 85%)`;
}

const createCard = (index) => {
    let newPost = post.cloneNode(true);
    console.log(newPost);
    newPost.childNodes[3].childNodes[1].innerText = quotes[Math.floor(Math.random() * quotes.length)];
    newPost.childNodes[1].src = urls[Math.floor(Math.random() * urls.length)];
    newPost.childNodes[1].addEventListener('dblclick', (evt) => {
        // Doubleclick the image to 'like' it
        evt.preventDefault();
        console.log('Clicked Like');
        newPost.childNodes[5].childNodes[1].style = "font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0,'opsz' 24";
    })
    newPost.style.backgroundColor = getRandomColor();
    newPost.childNodes[5].childNodes[1].addEventListener('click', (evt) => {
        // Click the  heart icon to 'like' it
        evt.preventDefault();
        console.log('Clicked Like');
        evt.target.style = "font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0,'opsz' 24";
    });
    newPost.childNodes[5].childNodes[3].addEventListener('click', (evt) => {
        // Open the image in a new tab
        evt.preventDefault();
        console.log('Clicked Open');
        window.open(newPost.childNodes[1].src, '_blank');
    });
    feed.appendChild(newPost);
}

const addPosts = (pageIndex) => {
    currentPage = pageIndex;

    const startRange = (pageIndex - 1) * cardIncrease;
    const endRange = currentPage == pageCount ? cardLimit : pageIndex * cardIncrease;

    for (let i = startRange + 1; i <= endRange; i++) {
        createCard(i);
    }
}

var throttleTimer;

const throttle = (callback, time) => {
    if (throttleTimer) return;

    throttleTimer = true;

    setTimeout(() => {
        callback();
        throttleTimer = false;
    }, time);
}

const handleInfiniteScroll = () => {
    throttle(() => {
        const endOfPage = window.innerHeight + window.scrollY >= document.body.offsetHeight;

        if (endOfPage) {
            // window.scrollTo(0, 100);
            addPosts(currentPage + 1);
        }
    }, 1000);
}

window.onload = function () {
    addPosts(currentPage);
    post.remove()
    post = document.getElementById('post');
}

window.addEventListener("scroll", handleInfiniteScroll);

var music = document.getElementById('music');
music.play();