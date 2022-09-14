import React from "react";

const ResultCaption = ({student:{Name,Year,Register_No}}) => {
    
    return(
        <div className="stud_caption">
        <p id="stud_name">Name : {Name}</p>
        <p id="stud_reg">Reg. no. : {Register_No}</p>
        <p id="stud_yr">Year & Dept : {Year} / IT</p>
        </div>
    );
}


export default ResultCaption;