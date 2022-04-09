import axios from 'axios'
export default{
    data(){

    },
    methods:{
        submit:function(){
            const path = 'http://127.0.0.1:5000/'
            axios.get(path).then(response => {
                console.log(response);
            }).catch(err => {
                console.log(err);
            });
        }
    }
}