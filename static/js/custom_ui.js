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

      <div class="chat-meta">now <span class="pull-right">Ward Admin</span></div>
     ${chatBox.value}
      <div class="clearfix"></div>
    </div>
  </li>
  <li class="by-me">

  <div class="avatar pull-left">
    <img src="/static/img/user.jpg" alt="" />
  </div>

  <div class="chat-content">

    <div class="chat-meta">Juma Kiwaka <span class="pull-right">now</span></div>
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
  const task = document.querySelectorAll('table.personal-task > tbody tr');



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
    todoDesc[0].value = todoDesc[1].value = todoDesc[2].value = '';
    task[task.length - 1].focus();
  })
}

function searchUser() {
  const searchForm = document.querySelector('form.search-form');
  const searchField = document.querySelector('form.search-form input');

  searchForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    let { value } = searchField;
    const tr = document.querySelectorAll('table.table > tbody tr');

    tr.forEach(trow => {
      let searchStr = `${trow.innerText}`;
      if (!searchStr.includes(value)) {
        trow.style.display = 'none';

      } else {
        trow.style.display = 'table-row';
      }

    });
    searchField.value = '';
  })

}

function applyBursary() {
  const applyForm = document.querySelector('form.apply-bursary');

  applyForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    const fields = applyForm.elements;
    for (let i = 0; i < fields.length - 1; i++) {
      const field = fields[i];
      console.log(field.value);
    }



    console.log('submitting form');

  })
}


