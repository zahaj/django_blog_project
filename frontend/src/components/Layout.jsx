// This component accepts 'children', which is a special React prop.
// It represents whatever is put *inside* the <Layout> tags.
function Layout({ children }) {
  return (
    <div className="app-container">
      <header>
        <h1>My React Portfolio</h1>
      </header>
      
      <main>
        {children}
      </main>
      
      <footer>
        <hr />
        <p>© 2025 Ewa Zahajkiewicz</p>
      </footer>
    </div>
  );
}

export default Layout;