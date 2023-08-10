const SHOW_SIDEBAR_BTN = document.querySelector('.show-sidebar')
const HIDE_SIDEBAR_BTN = document.querySelector('.hide-sidebar')
const SIDEBAR = document.querySelector('.sidebar')
const SEND_BTN = document.querySelector('.typing-textarea #send-btn')
const INPUT_AREA = document.querySelector('#chat-input')
const CHAT_CONTAINER = document.querySelector('.chat-container')

SHOW_SIDEBAR_BTN.addEventListener('click', () => {
    SIDEBAR.classList.add('show')
    SIDEBAR.classList.remove('hide')
})

HIDE_SIDEBAR_BTN.addEventListener('click', () => {
    SIDEBAR.classList.remove('show')
    SIDEBAR.classList.add('hide')
})

const sendMessage = () => {
    if(INPUT_AREA.value != '' && INPUT_AREA.value != ' '){
        const messageEl = document.createElement('div')
        messageEl.innerHTML = `<div class="user-container">
        <img src="../images/user.png" alt=""><p>${INPUT_AREA.value}</p>
    </div> 
    <div class="chatbot-container">
    <img src="../images/Asset+5.svg-removebg-preview - Copy.png" alt=""><p>No response to display</p>
    </div>`
        CHAT_CONTAINER.appendChild(messageEl)
        INPUT_AREA.value = ''
        CHAT_CONTAINER.scrollTop += CHAT_CONTAINER.clientHeight
    }
}

INPUT_AREA.addEventListener('keypress', (e) => {
    // console.log(e.target.value, 'oya')
    if(e.key == 'Enter'){
    console.log(e.target.value, 'oya')
        INPUT_AREA.value = ''
    }
})
INPUT_AREA.addEventListener('keydown', (e) => {
    if(e.key == 'Enter'){
        sendMessage()
    }
})
SEND_BTN.addEventListener('click', sendMessage)