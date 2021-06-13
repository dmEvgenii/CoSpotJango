
function init() { 
 
 // Создание карты.
    var myMap = new ymaps.Map("map", {
        center: [56, 37],
        zoom: 12,
    });
	
	myMap.geoObjects.add(part1.geojson);
}