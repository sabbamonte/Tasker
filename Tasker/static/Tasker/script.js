document.addEventListener('DOMContentLoaded', function() {

    add = document.querySelectorAll('.add')
    add.forEach((add_on) => {
        add_on.addEventListener('click', () => {
            add_task_or_note(add_on.value, add_on.name)
            
        })
    });

    checkmarks = document.querySelectorAll('.checkmark')
    checkmarks.forEach((checkmark) => {
        checkmark.addEventListener('click', Event => {
            const element = Event.target;
            if (element.className === "checkmark") {
                    check_task(checkmark.id, checkmark.checked)
                }
        });
    });

    delete_buttons = document.querySelectorAll('.delete')
    delete_buttons.forEach((button) => {
        button.addEventListener('click', () => {
            delete_task(button.id)
            
        })
    })

    filter = document.querySelectorAll('#filter')
    console.log(filter)
    filter.forEach((choice) => {
        choice.addEventListener('change', function() {
            var category = choice.options[choice.selectedIndex].value;
            console.log(category)
            filter_category(category)
        })
    })
    

    link = document.getElementById('delete_link')
    length = document.getElementById('delete_link').length
    if (length <= 4) {
        const element = document.createElement('button');
        element.innerHTML = `Add a link`
        element.className = `add_link btn btn-dark`
        document.querySelector("#link-view").append(element)
        element.addEventListener('click', () => {
            add_link(link.name)
        })
    }

    link.addEventListener('change', function() {
        link_to_delete = document.getElementById('delete_link')
        var link_subject = link_to_delete.options[link_to_delete.selectedIndex].id;
        var link_id = link_to_delete.options[link_to_delete.selectedIndex].className;
        document.querySelector('.link').addEventListener('click', () => {
            delete_link(link_subject, link_id)
        })
    })

    notes = document.querySelectorAll('.delete_note')
    notes.forEach((note) => {
        note.addEventListener('click', () => {
            delete_link(note.name, note.id)
        })  
    })

    edits = document.querySelectorAll('.note-items')
    edits.forEach((edit) => {
        edit.addEventListener('click', () => {
            var edit_name = edit.getAttribute('name')
            edit_note(edit.value, edit_name)
        })

    })  

    delete_notes = document.querySelectorAll('.delete_note')
    delete_notes.forEach((note) => {
        note.addEventListener('click', () => {
            var note_id = note.id
            var note_subject = note.getAttribute('name')
            delete_note(note_id, note_subject)
        })
    })

});

    function add_task_or_note(add_on_id, add_on_name) { 
        
        document.querySelector('.add').style.display = 'none'

        if (add_on_name === 'task') {
            const element = document.createElement('div')
            element.innerHTML = `<div class="alert alert-warning" role="alert">
            <strong>Don't forget to add a deadline!
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
            </div>`
            document.querySelector('.task-view').append(element)
            document.querySelector('.task').innerHTML = `<form id='save'><textarea rows="5" cols="50" id="newtask"></textarea> <br> <label for="deadline">Deadline:</label> <input type="date" id="date"> <button class="btn btn-dark" type="submit"> Save </button></form>`

            document.querySelector('#save').onsubmit = function() {

                fetch(`/add`, {
                    method: 'POST',
                    body: JSON.stringify({
                        task: document.querySelector('#newtask').value,
                        deadline: document.querySelector('#date').value
                    }) 
                }); 
                
            }
        }

        else {
            document.querySelector('.task').innerHTML = `<form id='save'><textarea rows="5" cols="50" id="newtext"></textarea> <br> <button class="btn btn-dark" type="submit"> Save </button></form>`
            
            document.querySelector('#save').onsubmit = function() {
            
                fetch(`/add`, {
                    method: 'POST',
                    body: JSON.stringify({
                        note: document.querySelector('#newtext').value,
                        subject: add_on_id
                    }) 
                });
            }
        }
    }

    function filter_category(category) {
        fetch(`/${category}`)
        .then(response => response.json())
        .then(filters => { 
            document.querySelector('#filter-view').innerHTML = "";
            Array.prototype.forEach.call(filters.filters, filter => {
                if (filter.category === category) {
                    document.querySelector('#subject-view').style.display = "none"
                    document.querySelector('#filter-view').style.display = "block"
                    var a = document.createElement('a')
                    var title = document.createElement('h4')
                    var link = document.createTextNode(`${filter.subject}`); 
                    a.appendChild(link);  
                    a.className = 'list-group-item list-group-item-action rounded-pill'
                    a.id = `${category}`
                    a.title = `${filter.subject}`; 
                    a.href = `subject/${filter.subject}`; 
                    title.append(a)
                    document.querySelector('#filter-view').appendChild(title)
                } 
                else {
                    document.querySelector('#subject-view').style.display = "block"
                    document.querySelector('#filter-view').style.display = "none"
                }
            })
        })
    }

    function add_link(link_name) {
        document.querySelector("#link-view").style.display = "none"
        document.querySelector("#add_link-view").style.display = "block"
        
        document.querySelector("#add_link-view").innerHTML = `<form id='add_link'><div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="URL" id="basic_url" aria-describedby="basic-addon3"> </div>
        <div class="input-group mb-3"> <input type="text" class="form-control" placeholder="Name" id="basic_name" aria-describedby="basic-addon3"> 
        </div> <button type="submit" class="add_link btn btn-dark" name="add_link">Add Link</button></form>`

        document.querySelector('#add_link').onsubmit = function() {
            fetch(`/add`, {
                method: 'POST',
                body: JSON.stringify({
                    name: document.querySelector('#basic_name').value,
                    subject: link_name,
                    link: document.querySelector('#basic_url').value
                }) 
            })
        }   
    }

    function check_task(task_id, status) {
            fetch(`/check/${task_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    checked: status
                })
            })
        var check_task = document.getElementById(`task-item-${task_id}`);
        check_task.remove();
    }

    function delete_task(task_id) {
        fetch(`delete/${task_id}`, {
            method: 'DELETE'
        })
        var task = document.getElementById(`${task_id}`);
        task.remove();
    }

    function delete_link(link_subject, link_id) {
        fetch(`${link_id}/delete/${link_subject}`, {
            method: 'DELETE'
        })
        var dropdown_option = document.getElementById(`${link_subject}`);
        dropdown_option.remove();
        var link = document.getElementById(`url-${link_subject}`);
        link.remove();
        var length = document.getElementById('delete_link').length
        if (length <= 1) {
            delete_button = document.querySelector('.link')
            delete_button.remove();
        } 
    }

    function delete_note(note_id, note_subject) {
        fetch(`${note_subject}/delete/${note_id}`, {
            method: 'DELETE'
        })
        document.getElementById(`${note_id}`).remove();
        document.getElementById(`note-${note_id}`).remove();
    }

    function edit_note(note_id, note_name) {
        fetch(`${note_name}/edit/${note_id}`)
        .then(response => response.json())
        .then(notes => {
            Array.prototype.forEach.call(notes.task, note => {
                console.log(note.note)
                console.log(note_id)
                document.querySelector(`#edit-note-${note.id}`).style.display == 'block'
                document.getElementById(`edit-note-${note.id}`).innerHTML = `<form id="edit_note"> <textarea rows="5" cols="45" id="newnote">${note.note}</textarea> <br> <button class="save_edit btn btn-dark" type="submit"> Save </button></form>`;

                document.querySelector('#edit_note').onsubmit = function() {
                    fetch(`${note_name}/edit/${note_id}`, {
                        method: 'PUT',
                        body: JSON.stringify({
                            note: document.querySelector('#newnote').value
                        })
                    })
                }
            })
        })
    }