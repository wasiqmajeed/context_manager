import xml.etree.ElementTree as ET

xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.03">
  <CstmrCdtTrfInitn>
    <GrpHdr>
      <MsgId>2024-03-12T19:30:00+01:00</MsgId>
      <CreDtTm>2024-03-12T19:30:00+01:00</CreDtTm>
      <NbOfTxs>2</NbOfTxs>
      <InitgPty>
        <Nm>Your Company Name</Nm>
        <Id>
          <OrgId>
            <Othr>
              <Id>1234567890</Id>
            </Othr>
          </OrgId>
        </Id>
      </InitgPty>
    </GrpHdr>
    <PmtInf>
      <PmtInfId>20240312001</PmtInfId>
      <PmtMtd>TRF</PmtMtd>
      <NbOfTxs>2</NbOfTxs>
      <CtrlSum>100.00</CtrlSum>
      <PmtTpInf>
        <SvcLvl>
          <Cd>SEPA</Cd>
        </SvcLvl>
        <LclInstr>
          <Cd>SEPA</Cd>
        </LclInstr>
      </PmtTpInf>
      <IntrBkSttlmDt>2024-03-15</IntrBkSttlmDt>
      <Dbtr>
        <Nm>Your Company Name</Nm>
        <Id>
          <OrgId>
            <Othr>
              <Id>1234567890</Id>
            </Othr>
          </OrgId>
        </Id>
        <PstlAdr>
          <Ctry>DE</Ctry>
          <AdrLine>123 Main Street</AdrLine>
          <CstmrTxInf>
            <PmtId>
              <EndToEndId>XYZ-12345</EndToEndId>
            </PmtId>
            <Amt>
              <InstdAmt Ccy="EUR">50.00</InstdAmt>
            </Amt>
            <Cdtr>
              <Nm>Vendor Name</Nm>
              <Id>
                <OrgId>
                  <Othr>
                    <Id>9876543210</Id>
                  </Othr>
                </OrgId>
              </Id>
              <PstlAdr>
                <Ctry>FR</Ctry>
                <AdrLine>45 Rue de la Paix</AdrLine>
              </PstlAdr>
            </Cdtr>
          </CstmrTxInf>
        </PstlAdr>
      </Dbtr>
      <DbtrAcct>
        <Id>
          <IBAN>DE12345678901234567890</IBAN>
        </Id>
      </DbtrAcct>
      <CdtTrfTxInf>
        <PmtId>
          <EndToEndId>XYZ-67890</EndToEndId>
        </PmtId>
        <Amt>
          <InstdAmt Ccy="EUR">50.00</InstdAmt>
        </Amt>
        <Cdtr>
          <Nm>Another Vendor Name</Nm>
          <Id>
            <OrgId>
              <Othr>
                <Id>0123456789</Id>
              </Othr>
            </OrgId>
          </Id>
          <PstlAdr>
            <Ctry>ES</Ctry>
            <AdrLine>16 Plaza Mayor</AdrLine>
          </PstlAdr>
        </Cdtr>
      </CdtTrfTxInf>
    </PmtInf>
  </CstmrCdtTrfInit
"""

with open("payment.xml", 'w') as f:
    f.write(xml_data)