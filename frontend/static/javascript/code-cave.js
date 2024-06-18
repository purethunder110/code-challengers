let GlobalEditorObject= null
let questionjudgement=false

//editor loader
document.addEventListener('DOMContentLoaded',(event)=>{
    require.config({ paths: { vs: '/node/monaco-editor/min/vs' } });
    require(['vs/editor/editor.main'], function () {
        var editor = monaco.editor.create(document.getElementById('code-editor'), {
        value:document.getElementById("code_data").value ,
        language: 'javascript',
        minimap:{"enabled": false},
        theme:"vs-dark"
        });
        GlobalEditorObject=editor
    });
});

//run code logic
document.getElementById("Run_code").addEventListener('click',function(){
    var source_code=GlobalEditorObject.getValue()
    var data={
        "platform":"python",
        "code":source_code
    }
    axios.post("/api/code-reciever/",data)
    .then(response=>{
        console.log(response.status)
        questionjudgement=response.data["judgement"]
    })
    .catch(error=>console.log(error))
})

//submit code logic
document.getElementById("submit_code").addEventListener("click",function(){
    if(questionjudgement){
        questionjudgement=false
        var question_timeline = document.querySelectorAll('#question-timeline .step');
        var flag=true
        for (let i=0;i<question_timeline.length-1;i++){
            //console.log(question_timeline[i])
            if (!question_timeline[i].classList.contains("step-primary") && flag){
                question_timeline[i].classList.add("step-primary")
                flag=false

                //getting the data
                axios.get("/api/new-question/")
                .then(response=>{
                    var quesobj=document.getElementById("Question-box")
                    quesobj.innerHTML=response.data["new-question"]
                })
            } 
        }
    }
})