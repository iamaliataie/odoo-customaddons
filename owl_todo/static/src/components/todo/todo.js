import { registry } from '@web/core/registry';
const { Component, useState } = owl;

export class OwlTodoList extends Component {
    setup(){
        this.state = useState(
            {value: 1}
        )
    }
}

registry.category('actions').add('owl.action_todo_list_js');