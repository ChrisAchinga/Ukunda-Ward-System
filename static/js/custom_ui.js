// the ui form for tertiary applicant -- appears when tertiary is selected from education level field
function toggleApplication() {
  const tertiaryForm = document.querySelector('.tertiary');
  const secondaryForm = document.querySelector('.secondary');

  const eduLevel = document.querySelector('#education-level').value;

  if (eduLevel === 'Tertiary') {
    secondaryForm.style.display = 'none';
    tertiaryForm.style.display = 'block';
  }
  else if (eduLevel === 'Secondary') {
    tertiaryForm.style.display = 'none';
    secondaryForm.style.display = 'block';
  }
  else {
    tertiaryForm.style.display = 'none';
    secondaryForm.style.display = 'none';
  }
}

// make fake chat ui
function sendChatMsg() {
  const chatForm = document.querySelector('form.chat-msg');
  const chatBox = document.querySelector('form.chat-msg input');
  const chatBin = document.querySelector('ul.chats');

  chatForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    chatBin.innerHTML += `<li class="by-other">

    <div class="avatar pull-right">
      <img src="/static/img/avatar1_small.jpg" alt="" />
    </div>

    <div class="chat-content">

      <div class="chat-meta">3 hours ago <span class="pull-right">Ward Admin</span></div>
     ${chatBox.value}
      <div class="clearfix"></div>
    </div>
  </li>
  <li class="by-me">

  <div class="avatar pull-left">
    <img src="/static/img/user.jpg" alt="" />
  </div>

  <div class="chat-content">

    <div class="chat-meta">Juma Kiwaka <span class="pull-right">3 hours ago</span></div>
    Hi!
    <div class="clearfix"></div>
  </div>
</li>`;

    chatBox.value = '';

  })
}

function addTodo() {
  const addTodoForm = document.querySelector('form.todo');
  const todoDesc = document.querySelectorAll('form.todo input');
  const tasks = document.querySelector('table.personal-task > tbody');

  addTodoForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    tasks.innerHTML += `
    <tr>
    <td>${todoDesc[1].value.replace('/', '-')}, ${todoDesc[2].value}</td>
    <td>
    ${todoDesc[0].value}
    </td>
    <td>
      <span class="badge bg-success">Task</span>
    </td>
    <td>
      <div id="work-progress3"></div>
    </td>
  </tr>`;
    console.log(todoDesc[2]);

  })
}

