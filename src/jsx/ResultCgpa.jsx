import React from "react";

const ResultCgpa = ({data:{GPA}}) => {
    return(
        <>
        <tr>
            <td className="unbordered"></td>
            <td className="unbordered"></td>
            <td>Total CGPA</td>
            <td className="cgpa_sec">{GPA}</td>
        </tr>
        </>
    );
}

export default ResultCgpa;