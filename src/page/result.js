import React from "react";
//import ResultBar from "../jsx/ResultBar";
import ResultVal from "../jsx/ResultVal";
import ResultTitle from "../jsx/ResultTitle";
import ResultCaption from "../jsx/ResultCaption";
import "./result.css"
import {data} from "../jsx/login.jsx"
import ResultCgpa from "../jsx/ResultCgpa";
import SubjectCode from "../page/subjectCode.json"





const ResultCard = () => {
    const arr=[];
    const Grade = [];
    const count = Object.keys(data).length;
    const keyys = Object.keys(data);

    
    for(let i=0;i<count;i++){
        if(keyys[i].length===9){
            arr.push(keyys[i])
        }
    }

    for(let j=0;j<arr.length;j++){
        const temp = JSON.parse('{}');
        const subGrad = arr[j]
        temp.SubCode=subGrad;
        const subjCode = subGrad.substring(1);
        temp.subTitle = SubjectCode[subjCode][0]
        temp.subSemester = SubjectCode[subjCode][1]
        const subVal = data[subGrad]
        temp.Grade=subVal;
        Grade.push(temp);
    }

    const Obj1 = '{}';
    const Student = JSON.parse(Obj1);
    Student.Name=data.Name;
    Student.GPA = data.GPA;
    Student.Register_No=data.Register_No;
    Student.DOB=data.DOB;
    Student.Marks = Grade;

    let temsem = 1;
    let stuYear = 0;
    for(let k=0;k<Student.Marks.length;k++){
        
    const semes = Object.values(Student.Marks[k])
    if(temsem<semes[2]){
        temsem=semes[2];
    }
    }

    if(temsem>6){
        stuYear="IV";        
    }else if(temsem>4){
        stuYear="III";
    }else if(temsem>2){
        stuYear="II";
    }else if(temsem>0){
        stuYear="I";
    }else{
        stuYear="Year Not Available"
    }
    Student.Year=stuYear;

    function GoBack(){
        window.history.back()
    }


    return(
        <>
        <div className="container">
        <button onClick={GoBack}>Back</button>
        <ResultCaption student={Student}/>
            <table>
                <ResultTitle />
                <tbody>
                <ResultVal data={Grade}/>
                <ResultCgpa data={Student}/>
                </tbody>
                </table>
        </div>
        </>
    );
}

export default ResultCard;