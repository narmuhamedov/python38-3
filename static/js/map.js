var map;

DG.then(function () {
    map = DG.map('map', {
        center: [42.880327, 74.586287],
        zoom: 13
    });

    DG.marker([42.880327, 74.586287]).addTo(map).bindPopup('Вы кликнули по мне!');
});