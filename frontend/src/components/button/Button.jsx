import React from 'react'

// fill, ghost, shadow, text

const Button = (props) => {

  let button;

  if (props.type == "fill") {
  button = <button className='btn button-fill'>{props.children}</button>
} else if  (props.type == "outline") {
  button = <button className='btn button-ghost'>{props.children}</button>
} else if  (props.type == "shadow") {
  button = <button className='btn button-shadow'>{props.children}</button>
} else if  (props.type == "shadow") {
  button = <button className='btn button-text'>{props.children}</button>
}

return {button}
}

export default Button