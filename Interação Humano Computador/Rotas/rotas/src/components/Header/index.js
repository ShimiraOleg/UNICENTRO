import { Link } from "react-router-dom";

function Header(){
    return(
        <header>

            <h2>Mateus de Oliveira Lopes</h2>
            
            <div>
                <Link to='/'>Home</Link>
                <Link to='/sobre'>Sobre</Link>
                <Link to='/contato'>Contato</Link>
                <Link to='/produto'>Produto</Link>
            </div>
        </header>
    );
}

export default Header;