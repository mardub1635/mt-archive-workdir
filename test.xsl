<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="pages/page/textbox/textline">
    <xsl:text>
        totot
    </xsl:text>
<xsl:for-each select="text[font='TimesNewRoman,Bold']">
<xsl:value-of select="." />

</xsl:for-each>
</xsl:template>


</xsl:stylesheet>

<!--<xsl:template match="text[@font='TimesNewRoman,Bold']"><xsl:value-of select="." /></xsl:template>
<xsl:template match="page">
    
<xsl:apply-templates/>

</xsl:template>
</xsl:stylesheet>-->
<!--<xsl:text>-->
<!--</xsl:text>-->
<!--</xsl:for-each>-->


