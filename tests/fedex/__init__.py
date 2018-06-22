'''

shipper = {"address": {"postal_code":"H3N1S4", "country_code":"CA"}}
recipient = {"address": {"city":"Lome", "country_code":"TG"}}
shipment_details = {"packages": [{"id":"1", "height":3, "lenght":10, "width":3,"weight":4.0}]}
from openship.mappers.fedex import  FedexClient
client = FedexClient(...)
from openship.mappers.fedex import FedexProxy
fedexProxy = FedexProxy(client)
from openship.domain.entities import Quote
payload = Quote.create(shipper=shipper, recipient=recipient, shipment_details=shipment_details)
request = fedexProxy.mapper.create_quote_request(payload)
response = fedexProxy.get_quotes(request)
quotes = fedexProxy.mapper.parse_quote_response(response)
print(jsonify(quotes))

'''



'''
<?xml version="1.0" ?>
<ns:RateReply xmlns:ns="http://fedex.com/ws/rate/v22">
    <ns:HighestSeverity>NOTE</ns:HighestSeverity>
    <ns:Notifications>
        <ns:Severity>NOTE</ns:Severity>
        <ns:Source>crs</ns:Source>
        <ns:Code>825</ns:Code>
        <ns:Message>The routing code was derived from the city for the destination. </ns:Message>
        <ns:LocalizedMessage>The routing code was derived from the city for the destination. </ns:LocalizedMessage>
        <ns:MessageParameters>
            <ns:Id>ORIGIN_OR_DESTINATION</ns:Id>
            <ns:Value>destination</ns:Value>
        </ns:MessageParameters>
    </ns:Notifications>
    <ns:TransactionDetail>
        <ns:CustomerTransactionId>FTC</ns:CustomerTransactionId>
    </ns:TransactionDetail>
    <ns:Version>
        <ns:ServiceId>crs</ns:ServiceId>
        <ns:Major>22</ns:Major>
        <ns:Intermediate>0</ns:Intermediate>
        <ns:Minor>0</ns:Minor>
    </ns:Version>
    <ns:RateReplyDetails>
        <ns:ServiceType>INTERNATIONAL_PRIORITY</ns:ServiceType>
        <ns:PackagingType>YOUR_PACKAGING</ns:PackagingType>
        <ns:DestinationAirportId>BRU</ns:DestinationAirportId>
        <ns:IneligibleForMoneyBackGuarantee>false</ns:IneligibleForMoneyBackGuarantee>
        <ns:OriginServiceArea>AM</ns:OriginServiceArea>
        <ns:DestinationServiceArea>PM</ns:DestinationServiceArea>
        <ns:SignatureOption>SERVICE_DEFAULT</ns:SignatureOption>
        <ns:ActualRateType>PAYOR_ACCOUNT_SHIPMENT</ns:ActualRateType>
        <ns:RatedShipmentDetails>
            <ns:EffectiveNetDiscount>
                <ns:Currency>USD</ns:Currency>
                <ns:Amount>0.</ns:Amount>
            </ns:EffectiveNetDiscount>
            <ns:ShipmentRateDetail>
                <ns:RateType>PAYOR_ACCOUNT_SHIPMENT</ns:RateType>
                <ns:RateScale>0000000</ns:RateScale>
                <ns:RateZone>CA003O</ns:RateZone>
                <ns:PricingCode>ACTUAL</ns:PricingCode>
                <ns:RatedWeightMethod>ACTUAL</ns:RatedWeightMethod>
                <ns:CurrencyExchangeRate>
                    <ns:FromCurrency>CAD</ns:FromCurrency>
                    <ns:IntoCurrency>USD</ns:IntoCurrency>
                    <ns:Rate>0.83</ns:Rate>
                </ns:CurrencyExchangeRate>
                <ns:DimDivisor>139</ns:DimDivisor>
                <ns:DimDivisorType>COUNTRY</ns:DimDivisorType>
                <ns:FuelSurchargePercent>4.</ns:FuelSurchargePercent>
                <ns:TotalBillingWeight>
                    <ns:Units>LB</ns:Units>
                    <ns:Value>4.</ns:Value>
                </ns:TotalBillingWeight>
                <ns:TotalBaseCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>230.490000000000009</ns:Amount>
                </ns:TotalBaseCharge>
                <ns:TotalFreightDiscounts>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalFreightDiscounts>
                <ns:TotalNetFreight>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>230.490000000000009</ns:Amount>
                </ns:TotalNetFreight>
                <ns:TotalSurcharges>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>9.220000000000001</ns:Amount>
                </ns:TotalSurcharges>
                <ns:TotalNetFedExCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetFedExCharge>
                <ns:TotalTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalTaxes>
                <ns:TotalNetCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetCharge>
                <ns:TotalRebates>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalRebates>
                <ns:TotalDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesAndTaxes>
                <ns:TotalAncillaryFeesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalAncillaryFeesAndTaxes>
                <ns:TotalDutiesTaxesAndFees>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesTaxesAndFees>
                <ns:TotalNetChargeWithDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetChargeWithDutiesAndTaxes>
                <ns:Surcharges>
                    <ns:SurchargeType>FUEL</ns:SurchargeType>
                    <ns:Description>Fuel</ns:Description>
                    <ns:Amount>
                        <ns:Currency>USD</ns:Currency>
                        <ns:Amount>9.220000000000001</ns:Amount>
                    </ns:Amount>
                </ns:Surcharges>
            </ns:ShipmentRateDetail>
        </ns:RatedShipmentDetails>
        <ns:RatedShipmentDetails>
            <ns:ShipmentRateDetail>
                <ns:RateType>PAYOR_LIST_SHIPMENT</ns:RateType>
                <ns:RateScale>0000000</ns:RateScale>
                <ns:RateZone>CA003O</ns:RateZone>
                <ns:PricingCode>ACTUAL</ns:PricingCode>
                <ns:RatedWeightMethod>ACTUAL</ns:RatedWeightMethod>
                <ns:CurrencyExchangeRate>
                    <ns:FromCurrency>CAD</ns:FromCurrency>
                    <ns:IntoCurrency>USD</ns:IntoCurrency>
                    <ns:Rate>0.83</ns:Rate>
                </ns:CurrencyExchangeRate>
                <ns:DimDivisor>139</ns:DimDivisor>
                <ns:DimDivisorType>COUNTRY</ns:DimDivisorType>
                <ns:FuelSurchargePercent>4.</ns:FuelSurchargePercent>
                <ns:TotalBillingWeight>
                    <ns:Units>LB</ns:Units>
                    <ns:Value>4.</ns:Value>
                </ns:TotalBillingWeight>
                <ns:TotalBaseCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>230.490000000000009</ns:Amount>
                </ns:TotalBaseCharge>
                <ns:TotalFreightDiscounts>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalFreightDiscounts>
                <ns:TotalNetFreight>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>230.490000000000009</ns:Amount>
                </ns:TotalNetFreight>
                <ns:TotalSurcharges>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>9.220000000000001</ns:Amount>
                </ns:TotalSurcharges>
                <ns:TotalNetFedExCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetFedExCharge>
                <ns:TotalTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalTaxes>
                <ns:TotalNetCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetCharge>
                <ns:TotalRebates>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalRebates>
                <ns:TotalDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesAndTaxes>
                <ns:TotalAncillaryFeesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalAncillaryFeesAndTaxes>
                <ns:TotalDutiesTaxesAndFees>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesTaxesAndFees>
                <ns:TotalNetChargeWithDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>239.710000000000008</ns:Amount>
                </ns:TotalNetChargeWithDutiesAndTaxes>
                <ns:Surcharges>
                    <ns:SurchargeType>FUEL</ns:SurchargeType>
                    <ns:Description>Fuel</ns:Description>
                    <ns:Amount>
                        <ns:Currency>USD</ns:Currency>
                        <ns:Amount>9.220000000000001</ns:Amount>
                    </ns:Amount>
                </ns:Surcharges>
            </ns:ShipmentRateDetail>
        </ns:RatedShipmentDetails>
    </ns:RateReplyDetails>
    <ns:RateReplyDetails>
        <ns:ServiceType>INTERNATIONAL_ECONOMY</ns:ServiceType>
        <ns:PackagingType>YOUR_PACKAGING</ns:PackagingType>
        <ns:DestinationAirportId>BRU</ns:DestinationAirportId>
        <ns:IneligibleForMoneyBackGuarantee>false</ns:IneligibleForMoneyBackGuarantee>
        <ns:OriginServiceArea>AM</ns:OriginServiceArea>
        <ns:DestinationServiceArea>PM</ns:DestinationServiceArea>
        <ns:SignatureOption>SERVICE_DEFAULT</ns:SignatureOption>
        <ns:ActualRateType>PAYOR_ACCOUNT_SHIPMENT</ns:ActualRateType>
        <ns:RatedShipmentDetails>
            <ns:EffectiveNetDiscount>
                <ns:Currency>USD</ns:Currency>
                <ns:Amount>0.</ns:Amount>
            </ns:EffectiveNetDiscount>
            <ns:ShipmentRateDetail>
                <ns:RateType>PAYOR_ACCOUNT_SHIPMENT</ns:RateType>
                <ns:RateScale>0000000</ns:RateScale>
                <ns:RateZone>CA003O</ns:RateZone>
                <ns:PricingCode>ACTUAL</ns:PricingCode>
                <ns:RatedWeightMethod>ACTUAL</ns:RatedWeightMethod>
                <ns:CurrencyExchangeRate>
                    <ns:FromCurrency>CAD</ns:FromCurrency>
                    <ns:IntoCurrency>USD</ns:IntoCurrency>
                    <ns:Rate>0.83</ns:Rate>
                </ns:CurrencyExchangeRate>
                <ns:DimDivisor>139</ns:DimDivisor>
                <ns:DimDivisorType>COUNTRY</ns:DimDivisorType>
                <ns:FuelSurchargePercent>4.</ns:FuelSurchargePercent>
                <ns:TotalBillingWeight>
                    <ns:Units>LB</ns:Units>
                    <ns:Value>4.</ns:Value>
                </ns:TotalBillingWeight>
                <ns:TotalBaseCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>207.469999999999999</ns:Amount>
                </ns:TotalBaseCharge>
                <ns:TotalFreightDiscounts>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalFreightDiscounts>
                <ns:TotalNetFreight>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>207.469999999999999</ns:Amount>
                </ns:TotalNetFreight>
                <ns:TotalSurcharges>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>8.300000000000001</ns:Amount>
                </ns:TotalSurcharges>
                <ns:TotalNetFedExCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetFedExCharge>
                <ns:TotalTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalTaxes>
                <ns:TotalNetCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetCharge>
                <ns:TotalRebates>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalRebates>
                <ns:TotalDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesAndTaxes>
                <ns:TotalAncillaryFeesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalAncillaryFeesAndTaxes>
                <ns:TotalDutiesTaxesAndFees>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesTaxesAndFees>
                <ns:TotalNetChargeWithDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetChargeWithDutiesAndTaxes>
                <ns:Surcharges>
                    <ns:SurchargeType>FUEL</ns:SurchargeType>
                    <ns:Description>Fuel</ns:Description>
                    <ns:Amount>
                        <ns:Currency>USD</ns:Currency>
                        <ns:Amount>8.300000000000001</ns:Amount>
                    </ns:Amount>
                </ns:Surcharges>
            </ns:ShipmentRateDetail>
        </ns:RatedShipmentDetails>
        <ns:RatedShipmentDetails>
            <ns:ShipmentRateDetail>
                <ns:RateType>PAYOR_LIST_SHIPMENT</ns:RateType>
                <ns:RateScale>0000000</ns:RateScale>
                <ns:RateZone>CA003O</ns:RateZone>
                <ns:PricingCode>ACTUAL</ns:PricingCode>
                <ns:RatedWeightMethod>ACTUAL</ns:RatedWeightMethod>
                <ns:CurrencyExchangeRate>
                    <ns:FromCurrency>CAD</ns:FromCurrency>
                    <ns:IntoCurrency>USD</ns:IntoCurrency>
                    <ns:Rate>0.83</ns:Rate>
                </ns:CurrencyExchangeRate>
                <ns:DimDivisor>139</ns:DimDivisor>
                <ns:DimDivisorType>COUNTRY</ns:DimDivisorType>
                <ns:FuelSurchargePercent>4.</ns:FuelSurchargePercent>
                <ns:TotalBillingWeight>
                    <ns:Units>LB</ns:Units>
                    <ns:Value>4.</ns:Value>
                </ns:TotalBillingWeight>
                <ns:TotalBaseCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>207.469999999999999</ns:Amount>
                </ns:TotalBaseCharge>
                <ns:TotalFreightDiscounts>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalFreightDiscounts>
                <ns:TotalNetFreight>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>207.469999999999999</ns:Amount>
                </ns:TotalNetFreight>
                <ns:TotalSurcharges>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>8.300000000000001</ns:Amount>
                </ns:TotalSurcharges>
                <ns:TotalNetFedExCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetFedExCharge>
                <ns:TotalTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalTaxes>
                <ns:TotalNetCharge>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetCharge>
                <ns:TotalRebates>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalRebates>
                <ns:TotalDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesAndTaxes>
                <ns:TotalAncillaryFeesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalAncillaryFeesAndTaxes>
                <ns:TotalDutiesTaxesAndFees>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>0.</ns:Amount>
                </ns:TotalDutiesTaxesAndFees>
                <ns:TotalNetChargeWithDutiesAndTaxes>
                    <ns:Currency>USD</ns:Currency>
                    <ns:Amount>215.77000000000001</ns:Amount>
                </ns:TotalNetChargeWithDutiesAndTaxes>
                <ns:Surcharges>
                    <ns:SurchargeType>FUEL</ns:SurchargeType>
                    <ns:Description>Fuel</ns:Description>
                    <ns:Amount>
                        <ns:Currency>USD</ns:Currency>
                        <ns:Amount>8.300000000000001</ns:Amount>
                    </ns:Amount>
                </ns:Surcharges>
            </ns:ShipmentRateDetail>
        </ns:RatedShipmentDetails>
    </ns:RateReplyDetails>
</ns:RateReply>
'''

'''
[
    [
        {
            "base_charge": 230.49,
            "carrier": "Fedex",
            "delivery_date": null,
            "delivery_time": null,
            "discount": 0.0,
            "duties_and_taxes": 0.0,
            "extra_charges": [
                {
                    "name": "FUEL",
                    "value": 9.22
                }
            ],
            "pickup_date": null,
            "pickup_time": null,
            "service_name": "INTERNATIONAL_PRIORITY",
            "service_type": "PAYOR_ACCOUNT_SHIPMENT",
            "total_charge": 239.71
        },
        {
            "base_charge": 207.47,
            "carrier": "Fedex",
            "delivery_date": null,
            "delivery_time": null,
            "discount": 0.0,
            "duties_and_taxes": 0.0,
            "extra_charges": [
                {
                    "name": "FUEL",
                    "value": 8.3
                }
            ],
            "pickup_date": null,
            "pickup_time": null,
            "service_name": "INTERNATIONAL_ECONOMY",
            "service_type": "PAYOR_ACCOUNT_SHIPMENT",
            "total_charge": 215.77
        }
    ],
    []
]
'''