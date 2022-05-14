const dice = document.querySelector('.dice');

dice.addEventListener('click', () => {
    getData();
});

function getData() {
    const url = `http://172.20.41.158:8080/location/attraction?long=50.061886117001634&lat=19.93860295517751`;
    fetch(url, {
            mode: 'cors',
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        })
        .then(response => response.json())
        .then(data => {
            createCard(
                data.attraction.image,
                data.attraction.name,
                data.attraction.score,
            );
        });
}

function createCard(src, cardTitle, score) {
    const card = document.querySelector(".card");
    const template = document.querySelector('#subcard');
    const clone = template.content.cloneNode(true);
    const img = clone.querySelector("img");
    const title = clone.querySelector("#title");
    const distance = clone.querySelector("#distance");
    const points = clone.querySelector("#points");

    img.src = src;
    title.innerText = cardTitle;
    points.innerText = score;

    card.innerHTML = '';
    card.appendChild(clone);
}