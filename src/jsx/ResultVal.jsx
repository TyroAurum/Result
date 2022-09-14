//import React from "react";
import ResultBar from "./ResultBar";


const ResultVal = ({data}) => {

    return(
        <>
        {data.map((elem)=>(<ResultBar student={elem}/>))}
        </>
    );
};

export default ResultVal;