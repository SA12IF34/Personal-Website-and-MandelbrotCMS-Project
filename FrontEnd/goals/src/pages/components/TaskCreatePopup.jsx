

function TaskCreatePopup({contentRef}) {



  return (
    <div className='task-popup'>
      <textarea ref={contentRef} placeholder='Mission Content' ></textarea>
      <button id='add-task-btn'>Add</button>
    </div>
  )
}

export default TaskCreatePopup;