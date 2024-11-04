let rpmGauge;
const maxRPM = 6600;
const maxSpeed = 220;
const gearRatios = [0, 45, 30, 20, 15, 10, 7.5]; // 0번 인덱스는 사용하지 않음
const minAngle = -225; // 게이지의 최소 각도
const maxAngle = 45;   // 게이지의 최대 각도

let currentRPM = 0;
let currentSpeed = 0;
let targetRPM = 0;
let targetSpeed = 0;

function createGauge(elementId, maxValue, color) {
    const ctx = document.getElementById(elementId).getContext('2d');
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [0, maxValue],
                backgroundColor: [color, '#333333'],
                borderWidth: 0
            }]
        },
        options: {
            circumference: 270,
            rotation: 225,
            cutout: '70%',
            responsive: false,
            maintainAspectRatio: true,
            animation: {
                duration: 100
            },
            plugins: {
                tooltip: { enabled: false },
                legend: { display: false }
            }
        }
    });
}

function initGauge() {
    rpmGauge = createGauge('rpm-gauge', maxRPM, '#ff0000');
}

function updateRPMGauge(rpm, gear, speed) {
    rpmGauge.data.datasets[0].data[0] = rpm;
    rpmGauge.data.datasets[0].data[1] = maxRPM - rpm;
    rpmGauge.update();
    document.getElementById('rpm-value').textContent = `${Math.round(rpm)} RPM`;

    const lowerGear = Math.max(1, gear - 1);
    const higherGear = Math.min(6, gear + 1);

    const lowerGearRPM = Math.max(0, rpm - 1000);
    const higherGearRPM = Math.min(maxRPM, rpm + 500);

    updateGearIndicator('lower-gear-indicator', 'lower-gear-label', lowerGearRPM, lowerGear);
    updateGearIndicator('higher-gear-indicator', 'higher-gear-label', higherGearRPM, higherGear);
}

function updateGearIndicator(indicatorId, labelId, gearRPM, gear) {
    const angle = (gearRPM / maxRPM) * 270 - 135; // 새로운 기준 각도 설정
    const indicator = document.getElementById(indicatorId);
    indicator.style.transform = `rotate(${angle}deg)`;

    const label = document.getElementById(labelId);
    label.textContent = gear;
}

function getGear(rpm, speed) {
    if (speed === 0) return 1;
    const ratio = rpm / speed;
    for (let i = 1; i < gearRatios.length; i++) {
        if (ratio > gearRatios[i]) return i;
    }
    return 6;
}

function updateDashboard() {
    // 현재 값을 목표 값에 점진적으로 접근시킵니다.
    currentRPM += (targetRPM - currentRPM) * 0.2;
    currentSpeed += (targetSpeed - currentSpeed) * 0.2;

    const gear = getGear(currentRPM, currentSpeed);
    updateRPMGauge(currentRPM, gear, currentSpeed);
    document.getElementById('speed-value').textContent = `${Math.round(currentSpeed)} km/h`;
    document.getElementById('gear-value').textContent = gear;
}

// 서버에서 데이터를 받아오는 함수 (예시)
function fetchData() {
    // 실제 구현시에는 WebSocket 또는 서버 API를 사용하여 데이터를 가져옵니다.
    // 이 예제에서는 랜덤 값을 생성합니다.
    targetRPM = Math.random() * maxRPM;
    targetSpeed = Math.random() * maxSpeed;
}

// 초기화 및 주기적 업데이트
initGauge();
setInterval(fetchData, 1000); // 1초마다 새로운 목표 데이터 생성
setInterval(updateDashboard, 50); // 50ms마다 대시보드 업데이트 (초당 20프레임)