function Signup({ data }) {
    return (
        <>
        signup.js
        </>
    )
}






// This gets called on every request
export async function getServerSideProps() {
    // Fetch data from external API
    const res = await fetch(`http://localhost:8000/api/get-posts/`)
    const data = await res.json()
  
    // Pass data to the page via props
    return { props: { data } }
  }
  
  
  
export default Signup;