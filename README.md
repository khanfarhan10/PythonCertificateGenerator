# PythonCertificateGenerator
Certificate Generator in Python using PDF/DOCX/Images.

### PDFs
Make Sure to use All Characters A-Za-z etc as text replacement for placeholders.

<blockquote>For best results use capitalizations using A-Z</blockquote>

From the repos :
Character replacement
One of the PDF format's strengths is that it embeds font information so that documents can be displayed even if the fonts used to create the PDF aren't available when the PDF is viewed. Most PDFs are optimized to only embed the font information for characters that are actually used in the document. So if a document doesn't contain a particular letter or symbol, information for rendering the letter or symbol is not stored in the PDF.

This has an unfortunate consequence for redaction in the text layer. Since redaction in the text layer works by performing simple text substitution in the text stream, you may create replacement text that contains characters that were not previously in the PDF. Those characters simply won't show up when the PDF is viewed because the PDF didn't contain any information about how to display them.

To get around this problem, pdf_redactor checks your replacement text for new characters and replaces them with characters from the content_replacement_glyphs list (defaulting to ?, #, *, and a space) if any of those characters are present in the font information already stored in the PDF. Hopefully at least one of those characters is present (maybe none are!), and in that case your replacement text will at least show up as something and not disappear.

Tools used under the hood :
- https://github.com/JoshData/pdf-redactor
- https://github.com/pmaupin/pdfrw
