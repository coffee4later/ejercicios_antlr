import org.antlr.v4.runtime.*;

public class ejercicio9 {
    public static void main(String[] args) throws Exception {
        // Leer desde terminal
        String input = System.console().readLine("> ");

        // Desde archivo
        // CharStream charStream = CharStreams.fromFileName(args[0]);

        CharStream charStream = CharStreams.fromString(input);

        // Crear lexer
        ExprLexer lexer = new ExprLexer(charStream);

        // Crear token stream
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        tokens.fill();

        System.out.println(tokens);

        // Iterar sobre los tokens
        for (Token token : tokens.getTokens()) {
            System.out.println("texto: " + token.getText());
            System.out.println("Linea: " + token.getLine());
            System.out.println("columna: " + token.getCharPositionInLine());
            System.out.println("nombre: " + lexer.getVocabulary().getSymbolicName(token.getType()));
            System.out.println("tipo: " + token.getType());
            System.out.println("----------------------------------------------");
        }
    }
}