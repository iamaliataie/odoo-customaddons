/** @odoo-module **/
 
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from '@web/core/utils/hooks';

export class OwlTodoList extends Component {
    setup(){
        this.state = useState(
            {
                task: {
                    name: "",
                    color: "#00000",
                    completed: false,
                },
                taskList: [],
                isEditable: false,
                activeId: null,
            }
        )
        this.orm = useService("orm")
        this.model = "owl.todo.list"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllTask()
        })
    }

    async getAllTask () {
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name","color","completed"])
    }

    async saveTask() {
        if (this.state.isEditable){
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        else {
            await this.orm.create(this.model, [this.state.task])
        }

        await this.getAllTask()
    }

    addTask() {
        this.resetForm()
        this.state.activeId = null
        this.state.isEditable = false
    }

    editTask(task) {
        this.state.isEditable = true
        this.state.activeId = task.id
        this.state.task = {...task}
    }

    async deleteTask(task) {
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTask()

    }

    async searchTask() {
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model, [["name", "ilike", text]], ["name", "color", "completed"])
    }

    async toggleStatus(e, task) {
        await this.orm.write(this.model, [task.id], {completed: e.target.checked})
        await this.getAllTask()
    }

    async toggleColor(e, task) {
        await this.orm.write(this.model, [task.id], {color: e.target.value})
        await this.getAllTask()
    }

    resetForm() {
        this.state.task = {name: "", color: "#000", completed: false}
    }
}

OwlTodoList.template = 'owl.TodoList'
registry.category('actions').add('owl.action_todo_list_js', OwlTodoList);