let GlobalEditorObject= null
let questionjudgement=false

//editor loader
document.addEventListener('DOMContentLoaded',(event)=>{
    //editor load
    require.config({ paths: { vs: '/node/monaco-editor/min/vs' } });
    require(['vs/editor/editor.main'], function () {
        var editor = monaco.editor.create(document.getElementById('code-editor'), {
        value:document.getElementById("code_data").value ,
        language: 'javascript',
        minimap:{"enabled": false},
        });
        GlobalEditorObject=editor
    });

    //theme load from setting
    var uitheme=window.localStorage.getItem("ui-theme")
    var editortheme=window.localStorage.getItem("editor-theme")
    //ui-theme load
    if (uitheme==null){
        window.localStorage.setItem("ui-theme","light")
        uitheme=window.localStorage.getItem("ui-theme")
    }
    window.localStorage.setItem("theme",uitheme)
    document.documentElement.setAttribute("data-theme",uitheme)

    //editortheme load
    if(editortheme==null){
        window.localStorage.setItem("editor-theme","vs")
    }
    else{
        //ADDING ASYNC DELAY SO THAT THE EDITOR CAN LOAD BEFORE CHANGING SAVED THEME
        setTimeout(function(){
            Change_editor_theme(editortheme,GlobalEditorObject)
        }, 200);
    }
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
                //step visable
                question_timeline[i].classList.add("step-primary")
                flag=false
                //display data
                var quesobj=document.getElementById("Question-box")
                quesobj.innerHTML="";
                document.getElementById("loading-question").style.display="block";

                //getting the data
                axios.get("/api/new-question/")
                .then(response=>{
                    document.getElementById("loading-question").style.display="none";
                    quesobj.innerHTML=response.data["new-question"]
                })
            } 
        }
    }
})