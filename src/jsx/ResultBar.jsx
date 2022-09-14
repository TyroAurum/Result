import React from "react";


const ResultBar = ({student:{SubCode,subTitle,subSemester,Grade}}) => {
    SubCode = SubCode.substring(1);
    return(
        <>
            <tr>
                <td>{subSemester}</td>
                <td>{SubCode}</td>
                <td>{subTitle}</td>
                <td id="grad_sec">{Grade}</td>
            </tr>
        </>
    );
}


export default ResultBar;
