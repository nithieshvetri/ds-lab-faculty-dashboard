import React, { useState, useEffect } from "react";

export default function Select(props) {
  const [options, setOptions] = useState([]);
  useEffect(() => {
    // props.onChange(props.id, "");
    const fetchList = async () => {
      const resp = await fetch(
        `api/faculty${props.url}/`
      );
      const data = await resp.json();
      // console.log(data);
      setOptions(data);
    };
    fetchList();
  }, [props.url]);
  const changeHandler = (e) => props.onChange(props.id, e.target.value);
  return (
    <div className="search-input-groups">
      <label>{props.label}</label>
      <select onClick={changeHandler}>
        {options.length > 0 &&
          options.map((x) => (
            <option value={x} key={x}>
              {x}
            </option>
          ))}
      </select>
    </div>
  );
}
