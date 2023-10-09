/** @odoo-module **/
 
import { registry } from '@web/core/registry';
const { Component, useState } = owl;

export class OwlTodoList extends Component {
    setup(){
        this.state = useState(
            {
                taskList: [
                    {
                        id: 1,
                        name: 'Task 1',
                        completed: true,
                        color: '#ff1155'
                    },
                    {
                        id: 2,
                        name: 'Task 2',
                        completed: true,
                        color: '#55ff11'
                    },
                    {
                        id: 3,
                        name: 'Task 3',
                        completed: true,
                        color: '#1155ff'
                    },
                ],
            }
        )
    }
}

OwlTodoList.template = 'owl.TodoList'

registry.category('actions').add('owl.action_todo_list_js', OwlTodoList);