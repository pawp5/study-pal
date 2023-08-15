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

    // const sendMessage = () => {
    //     if(INPUT_AREA.value != '' && INPUT_AREA.value != ' '){
    //         const messageEl = document.createElement('div')
    //         messageEl.innerHTML = `<div class="user-container">
    //         <img src="../images/user.png" alt=""><p>${INPUT_AREA.value}</p>
    //     </div> 
    //     <div class="chatbot-container">
    //       <i class="bi bi-robot"></i><p>No response to display</p>
    //     </div>`
    //         CHAT_CONTAINER.appendChild(messageEl)
    //         INPUT_AREA.value = ''
    //         CHAT_CONTAINER.scrollTop += CHAT_CONTAINER.clientHeight
    //     }
    // }
    // Get the CSRF token from the cookie
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
      }
      return cookieValue;
    }

    const sendMessage = () => {
      const userMessage = INPUT_AREA.value.trim(); // Remove leading and trailing whitespace

      if (userMessage !== '') {
          const messageEl = document.createElement('div');
          
          // Display user message
          messageEl.innerHTML = `<div class="user-container">
              <img src="{% static 'studypals/images/img/study.svg' %}" alt=""><p>${userMessage}</p>
          </div>`;
          
          CHAT_CONTAINER.appendChild(messageEl);
          INPUT_AREA.value = '';
          CHAT_CONTAINER.scrollTop += CHAT_CONTAINER.clientHeight;

          // Get the CSRF token
          const csrftoken = getCookie('csrftoken');

          // Send user message to the backend
          fetch('/chat/', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': csrftoken // Include the CSRF token in the request headers
                },
              body: JSON.stringify({ message: userMessage })
            })
          .then(response => response.json())// Response will be HTML content
          .then(data => {
              const botMessageEl = document.createElement('div');
              
              // Display chatbot response
              botMessageEl.innerHTML = `<div class="chatbot-container">
              <img src="{% static 'studypals/images/img/study.svg' %}" alt=""><p>${data.response}</p>
              </div>`;
              
              CHAT_CONTAINER.appendChild(botMessageEl);
              CHAT_CONTAINER.scrollTop += CHAT_CONTAINER.clientHeight;
            })
          .catch(error => {
              console.error('Error fetching chatbot response:', error);
          });
        }
    };


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