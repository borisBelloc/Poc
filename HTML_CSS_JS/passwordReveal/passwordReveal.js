Vue.component('input-password', {
	template:
		// the input password made by vue.js component
	    '<span class="input-password">' +
		'<input v-show="!visible" type="password" v-model="password" placeholder="password" name="password" id="password">' +
		'<input v-show="visible" type="text" v-model="password" placeholder="password">' + 
		'<button @click.prevent @mousedown.prevent="set_visible()" @mouseup.prevent="set_visible()" :class="{ visible: visible }"></button>' +
		'</span>',
	data: function() {
		return {
			password: 'password1234',
			visible: false
		}
	},
	methods: {
		set_visible: function() {
			this.visible = !this.visible;
		}
	}
});

var app = new Vue({
	el: '#app_reveal'
});