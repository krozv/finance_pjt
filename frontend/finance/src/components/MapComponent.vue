<template>
    <div id="map">test</div>
</template>

<script setup>
import { info } from 'sass';
import { ref, onMounted } from 'vue';

const apiKey = import.meta.env.VITE_API_KEY
const mapData = ref(null)
const currentPosition = ref(null);
const infowindow = ref(null)
onMounted(() => {
    getCurrentPosition()
    .then((res) => {
        console.log(res)
        currentPosition.value = {
            lat: res.coords.latitude,
            lon: res.coords.longitude,
        }
        return loadKakaoMap()
    })
    .then((res) => {
        console.log(res)
        return searchBank(res)
    })
    .catch((err) => {
        console.log(err)
    })
    // kakao 지도 API 동적 로드 방법
    
})

const loadKakaoMap = function () {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.type = 'text/javascript'
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${apiKey}&autoload=false&libraries=services`
        script.async = true
        script.onerror = () => {
            reject(new Error("Kakao 지도 API 스크립트 로드 실패"))
        }
        script.onload = () => {
            console.log('로드 완료')
            initMap().then((res) => resolve(res))}
        document.body.appendChild(script)
    })
}

// kakao 지도 API 로드 완료 후 실행할 초기화 함수
const initMap = function () {
    return new Promise((resolve, reject) => {
        if (!window.kakao || !window.kakao.maps) {
            reject(new Error('kakao 지도 API가 로드되지 않았습니다.'))
        }
        else {
            kakao.maps.load(() => {
                const container = document.getElementById('map')
                const latlng = new window.kakao.maps.LatLng(currentPosition.value.lat, currentPosition.value.lon)
                const options = {
                    center: latlng, // 내 위치 중심으로 지도 초기화
                    level: 4 // 지도 확대 레벨 설정
                }
                // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성합니다
                infowindow.value = new kakao.maps.InfoWindow({zIndex:1});
                mapData.value = new window.kakao.maps.Map(container, options)
                console.log('Kakao 지도 초기화 완료')
                const res = {
                    latlng: latlng,
                }
                resolve(res) // promise 성공 처리
        })}
    })}
    
// 현재 위치 받기
const getCurrentPosition = function () {
    return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(resolve, reject)
    }
    else {
        reject(new Error('Geolocation API 지원 X'))
    }
    })
}

// 은행 위치 검색하기
const searchBank = function (res) {
    return new Promise((resolve, reject) => {
        console.log(kakao.maps.services)
        const ps = new kakao.maps.services.Places()
        const displacePlaces = function(result, status){
            if (status === kakao.maps.services.Status.OK) {
                // console.log(result)
                for (var i=0; i<result.length; i++){
                    var marker = displayMarker(result[i], i, res);
                }
                resolve()
            } else {
                reject(new Error("Places API 검색 실패"))
            }
        }
        
        const options = {
            location: res.latlng,
            radius: 10000,
        }
        ps.keywordSearch('은행', displacePlaces, options)
    })
}

const displayMarker = function (place, idx, res) {
    var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
    imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
    imgOptions =  {
        spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
        spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
        offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
    },
    markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
        marker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(place.y, place.x), // 마커의 위치
        image: markerImage 
    });
    marker.setMap(mapData.value); // 지도 위에 마커를 표출합니다
    // markers.push(marker);  // 배열에 생성된 마커를 추가합니다
    const content = ref(null);
    (function(marker) {
        kakao.maps.event.addListener(marker, 'click', function() {
            // click event 수정하기
            if (content.value){
                infowindow.value.close();
                content.value = null
            }
            else {
                content.value = '<div style="padding:5px;z-index:1;">' + place.place_name + '</div>';
                infowindow.value.setContent(content.value);
                infowindow.value.open(mapData.value, marker);
            }
            
        });
    })(marker, place.place_name);
    return marker;
}

</script>

<style scoped>
#map {
    width: 500px;
    height: 400px;
}
</style>