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