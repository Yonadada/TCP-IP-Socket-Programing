let ledState = false; //  false = 꺼짐, true = 켜짐

function ledSwitchHandler(){
    const label = document.getElementById("ledLabel");

    //상태 뒤집
    ledState = !ledState;

    //서버에 fetch 요청보내기
    const state = ledState ? "on" : "off";
    const color = "red";

    fetch(`/dashboard/led?color=${color}&state=${state}`)
        .then(response => response.json())
        .then(data => {
            label.textContent = ledState ? "LED ON " : "LED OFF";

        })
        .catch(error => {
            console.error("LED 전송 실패", error);
            label.textContent = "에러";
        });
}

document.getElementById("ledSwitch").addEventListener("change", ledSwitchHandler);