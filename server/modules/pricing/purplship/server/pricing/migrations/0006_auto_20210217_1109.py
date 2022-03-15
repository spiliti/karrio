# Generated by Django 3.1.6 on 2021-02-17 11:09

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import functools
import karrio.server.core.fields
import karrio.server.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0005_auto_20210204_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surcharge',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(karrio.server.core.models.uuid, *(), **{'prefix': 'chrg_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The surcharge name (label) that will appear in the rate (quote)', max_length=100, unique=True)),
                ('amount', models.FloatField(help_text='The surcharge amount to add to the quote')),
                ('carriers', karrio.server.core.fields.MultiChoiceField(base_field=models.CharField(choices=[('aramex', 'aramex'), ('australiapost', 'australiapost'), ('canadapost', 'canadapost'), ('canpar', 'canpar'), ('dhl_express', 'dhl_express'), ('dhl_universal', 'dhl_universal'), ('dicom', 'dicom'), ('fedex_express', 'fedex_express'), ('purolator_courier', 'purolator_courier'), ('royalmail', 'royalmail'), ('sendle', 'sendle'), ('sf_express', 'sf_express'), ('ups_package', 'ups_package'), ('usps', 'usps'), ('yanwen', 'yanwen'), ('yunexpress', 'yunexpress'), ('freightcom', 'freightcom'), ('eshipper', 'eshipper')], max_length=50), blank=True, help_text='\n        The list of carriers you want to apply the surcharge to.\n        \n        Note that by default, the surcharge is applied to all carriers\n        ', null=True, size=None)),
                ('services', karrio.server.core.fields.MultiChoiceField(base_field=models.CharField(choices=[('ups_standard', 'ups_standard'), ('ups_worldwide_expedited', 'ups_worldwide_expedited'), ('ups_worldwide_express', 'ups_worldwide_express'), ('ups_worldwide_express_plus', 'ups_worldwide_express_plus'), ('ups_worldwide_saver', 'ups_worldwide_saver'), ('ups_2nd_day_air', 'ups_2nd_day_air'), ('ups_2nd_day_air_am', 'ups_2nd_day_air_am'), ('ups_3_day_select', 'ups_3_day_select'), ('ups_expedited_mail_innovations', 'ups_expedited_mail_innovations'), ('ups_first_class_mail', 'ups_first_class_mail'), ('ups_ground', 'ups_ground'), ('ups_next_day_air', 'ups_next_day_air'), ('ups_next_day_air_early', 'ups_next_day_air_early'), ('ups_next_day_air_saver', 'ups_next_day_air_saver'), ('ups_priority_mail', 'ups_priority_mail'), ('ups_access_point_economy', 'ups_access_point_economy'), ('ups_today_dedicated_courier', 'ups_today_dedicated_courier'), ('ups_today_express', 'ups_today_express'), ('ups_today_express_saver', 'ups_today_express_saver'), ('ups_today_standard', 'ups_today_standard'), ('ups_worldwide_express_freight', 'ups_worldwide_express_freight'), ('ups_priority_mail_innovations', 'ups_priority_mail_innovations'), ('ups_economy_mail_innovations', 'ups_economy_mail_innovations'), ('purolator_express_9_am', 'purolator_express_9_am'), ('purolator_express_us', 'purolator_express_us'), ('purolator_express_10_30_am', 'purolator_express_10_30_am'), ('purolator_express_us_9_am', 'purolator_express_us_9_am'), ('purolator_express_12_pm', 'purolator_express_12_pm'), ('purolator_express_us_10_30_am', 'purolator_express_us_10_30_am'), ('purolator_express', 'purolator_express'), ('purolator_express_us_12_00', 'purolator_express_us_12_00'), ('purolator_express_evening', 'purolator_express_evening'), ('purolator_express_envelope_us', 'purolator_express_envelope_us'), ('purolator_express_envelope_9_am', 'purolator_express_envelope_9_am'), ('purolator_express_us_envelope_9_am', 'purolator_express_us_envelope_9_am'), ('purolator_express_envelope_10_30_am', 'purolator_express_envelope_10_30_am'), ('purolator_express_us_envelope_10_30_am', 'purolator_express_us_envelope_10_30_am'), ('purolator_express_envelope_12_pm', 'purolator_express_envelope_12_pm'), ('purolator_express_us_envelope_12_00', 'purolator_express_us_envelope_12_00'), ('purolator_express_envelope', 'purolator_express_envelope'), ('purolator_express_pack_us', 'purolator_express_pack_us'), ('purolator_express_envelope_evening', 'purolator_express_envelope_evening'), ('purolator_express_us_pack_9_am', 'purolator_express_us_pack_9_am'), ('purolator_express_pack_9_am', 'purolator_express_pack_9_am'), ('purolator_express_us_pack_10_30_am', 'purolator_express_us_pack_10_30_am'), ('purolator_express_pack10_30_am', 'purolator_express_pack10_30_am'), ('purolator_express_us_pack_12_00', 'purolator_express_us_pack_12_00'), ('purolator_express_pack_12_pm', 'purolator_express_pack_12_pm'), ('purolator_express_box_us', 'purolator_express_box_us'), ('purolator_express_pack', 'purolator_express_pack'), ('purolator_express_us_box_9_am', 'purolator_express_us_box_9_am'), ('purolator_express_pack_evening', 'purolator_express_pack_evening'), ('purolator_express_us_box_10_30_am', 'purolator_express_us_box_10_30_am'), ('purolator_express_box_9_am', 'purolator_express_box_9_am'), ('purolator_express_us_box_12_00', 'purolator_express_us_box_12_00'), ('purolator_express_box_10_30_am', 'purolator_express_box_10_30_am'), ('purolator_ground_us', 'purolator_ground_us'), ('purolator_express_box_12_pm', 'purolator_express_box_12_pm'), ('purolator_express_international', 'purolator_express_international'), ('purolator_express_box', 'purolator_express_box'), ('purolator_express_international_9_am', 'purolator_express_international_9_am'), ('purolator_express_box_evening', 'purolator_express_box_evening'), ('purolator_express_international_10_30_am', 'purolator_express_international_10_30_am'), ('purolator_ground', 'purolator_ground'), ('purolator_express_international_12_00', 'purolator_express_international_12_00'), ('purolator_ground9_am', 'purolator_ground9_am'), ('purolator_express_envelope_international', 'purolator_express_envelope_international'), ('purolator_ground10_30_am', 'purolator_ground10_30_am'), ('purolator_express_international_envelope_9_am', 'purolator_express_international_envelope_9_am'), ('purolator_ground_evening', 'purolator_ground_evening'), ('purolator_express_international_envelope_10_30_am', 'purolator_express_international_envelope_10_30_am'), ('purolator_quick_ship', 'purolator_quick_ship'), ('purolator_express_international_envelope_12_00', 'purolator_express_international_envelope_12_00'), ('purolator_quick_ship_envelope', 'purolator_quick_ship_envelope'), ('purolator_express_pack_international', 'purolator_express_pack_international'), ('purolator_quick_ship_pack', 'purolator_quick_ship_pack'), ('purolator_express_international_pack_9_am', 'purolator_express_international_pack_9_am'), ('purolator_quick_ship_box', 'purolator_quick_ship_box'), ('purolator_express_international_pack_10_30_am', 'purolator_express_international_pack_10_30_am'), ('purolator_express_international_pack_12_00', 'purolator_express_international_pack_12_00'), ('purolator_express_box_international', 'purolator_express_box_international'), ('purolator_express_international_box_9_am', 'purolator_express_international_box_9_am'), ('purolator_express_international_box_10_30_am', 'purolator_express_international_box_10_30_am'), ('purolator_express_international_box_12_00', 'purolator_express_international_box_12_00'), ('fedex_europe_first_international_priority', 'fedex_europe_first_international_priority'), ('fedex_1_day_freight', 'fedex_1_day_freight'), ('fedex_2_day', 'fedex_2_day'), ('fedex_2_day_am', 'fedex_2_day_am'), ('fedex_2_day_freight', 'fedex_2_day_freight'), ('fedex_3_day_freight', 'fedex_3_day_freight'), ('fedex_cargo_airport_to_airport', 'fedex_cargo_airport_to_airport'), ('fedex_cargo_freight_forwarding', 'fedex_cargo_freight_forwarding'), ('fedex_cargo_international_express_freight', 'fedex_cargo_international_express_freight'), ('fedex_cargo_international_premium', 'fedex_cargo_international_premium'), ('fedex_cargo_mail', 'fedex_cargo_mail'), ('fedex_cargo_registered_mail', 'fedex_cargo_registered_mail'), ('fedex_cargo_surface_mail', 'fedex_cargo_surface_mail'), ('fedex_custom_critical_air_expedite', 'fedex_custom_critical_air_expedite'), ('fedex_custom_critical_air_expedite_exclusive_use', 'fedex_custom_critical_air_expedite_exclusive_use'), ('fedex_custom_critical_air_expedite_network', 'fedex_custom_critical_air_expedite_network'), ('fedex_custom_critical_charter_air', 'fedex_custom_critical_charter_air'), ('fedex_custom_critical_point_to_point', 'fedex_custom_critical_point_to_point'), ('fedex_custom_critical_surface_expedite', 'fedex_custom_critical_surface_expedite'), ('fedex_custom_critical_surface_expedite_exclusive_use', 'fedex_custom_critical_surface_expedite_exclusive_use'), ('fedex_custom_critical_temp_assure_air', 'fedex_custom_critical_temp_assure_air'), ('fedex_custom_critical_temp_assure_validated_air', 'fedex_custom_critical_temp_assure_validated_air'), ('fedex_custom_critical_white_glove_services', 'fedex_custom_critical_white_glove_services'), ('fedex_distance_deferred', 'fedex_distance_deferred'), ('fedex_express_saver', 'fedex_express_saver'), ('fedex_first_freight', 'fedex_first_freight'), ('fedex_freight_economy', 'fedex_freight_economy'), ('fedex_freight_priority', 'fedex_freight_priority'), ('fedex_ground', 'fedex_ground'), ('fedex_international_priority_plus', 'fedex_international_priority_plus'), ('fedex_next_day_afternoon', 'fedex_next_day_afternoon'), ('fedex_next_day_early_morning', 'fedex_next_day_early_morning'), ('fedex_next_day_end_of_day', 'fedex_next_day_end_of_day'), ('fedex_next_day_freight', 'fedex_next_day_freight'), ('fedex_next_day_mid_morning', 'fedex_next_day_mid_morning'), ('fedex_first_overnight', 'fedex_first_overnight'), ('fedex_ground_home_delivery', 'fedex_ground_home_delivery'), ('fedex_international_distribution_freight', 'fedex_international_distribution_freight'), ('fedex_international_economy', 'fedex_international_economy'), ('fedex_international_economy_distribution', 'fedex_international_economy_distribution'), ('fedex_international_economy_freight', 'fedex_international_economy_freight'), ('fedex_international_first', 'fedex_international_first'), ('fedex_international_ground', 'fedex_international_ground'), ('fedex_international_priority', 'fedex_international_priority'), ('fedex_international_priority_distribution', 'fedex_international_priority_distribution'), ('fedex_international_priority_express', 'fedex_international_priority_express'), ('fedex_international_priority_freight', 'fedex_international_priority_freight'), ('fedex_priority_overnight', 'fedex_priority_overnight'), ('fedex_same_day', 'fedex_same_day'), ('fedex_same_day_city', 'fedex_same_day_city'), ('fedex_same_day_metro_afternoon', 'fedex_same_day_metro_afternoon'), ('fedex_same_day_metro_morning', 'fedex_same_day_metro_morning'), ('fedex_same_day_metro_rush', 'fedex_same_day_metro_rush'), ('fedex_smart_post', 'fedex_smart_post'), ('fedex_standard_overnight', 'fedex_standard_overnight'), ('fedex_transborder_distribution_consolidation', 'fedex_transborder_distribution_consolidation'), ('canadapost_regular_parcel', 'canadapost_regular_parcel'), ('canadapost_expedited_parcel', 'canadapost_expedited_parcel'), ('canadapost_xpresspost', 'canadapost_xpresspost'), ('canadapost_priority', 'canadapost_priority'), ('canadapost_library_books', 'canadapost_library_books'), ('canadapost_expedited_parcel_usa', 'canadapost_expedited_parcel_usa'), ('canadapost_priority_worldwide_envelope_usa', 'canadapost_priority_worldwide_envelope_usa'), ('canadapost_priority_worldwide_pak_usa', 'canadapost_priority_worldwide_pak_usa'), ('canadapost_priority_worldwide_parcel_usa', 'canadapost_priority_worldwide_parcel_usa'), ('canadapost_small_packet_usa_air', 'canadapost_small_packet_usa_air'), ('canadapost_tracked_packet_usa', 'canadapost_tracked_packet_usa'), ('canadapost_tracked_packet_usa_lvm', 'canadapost_tracked_packet_usa_lvm'), ('canadapost_xpresspost_usa', 'canadapost_xpresspost_usa'), ('canadapost_xpresspost_international', 'canadapost_xpresspost_international'), ('canadapost_international_parcel_air', 'canadapost_international_parcel_air'), ('canadapost_international_parcel_surface', 'canadapost_international_parcel_surface'), ('canadapost_priority_worldwide_envelope_intl', 'canadapost_priority_worldwide_envelope_intl'), ('canadapost_priority_worldwide_pak_intl', 'canadapost_priority_worldwide_pak_intl'), ('canadapost_priority_worldwide_parcel_intl', 'canadapost_priority_worldwide_parcel_intl'), ('canadapost_small_packet_international_air', 'canadapost_small_packet_international_air'), ('canadapost_small_packet_international_surface', 'canadapost_small_packet_international_surface'), ('canadapost_tracked_packet_international', 'canadapost_tracked_packet_international'), ('freightcom_all', 'freightcom_all'), ('freightcom_central_transport', 'freightcom_central_transport'), ('freigthcom_estes', 'freigthcom_estes'), ('freigthcom_usf_holland', 'freigthcom_usf_holland'), ('freightcom_dicom_ground', 'freightcom_dicom_ground'), ('freightcom_ground', 'freightcom_ground'), ('freightcom_select', 'freightcom_select'), ('freightcom_overnight', 'freightcom_overnight'), ('freightcom_purolator_ground', 'freightcom_purolator_ground'), ('freightcom_purolator_express', 'freightcom_purolator_express'), ('freightcom_purolator_express_9_am', 'freightcom_purolator_express_9_am'), ('freightcom_purolator_express_10_30_am', 'freightcom_purolator_express_10_30_am'), ('freightcom_fedex_express_saver', 'freightcom_fedex_express_saver'), ('freightcom_fedex_ground', 'freightcom_fedex_ground'), ('freightcom_fedex_2_day', 'freightcom_fedex_2_day'), ('freightcom_fedex_priority_overnight', 'freightcom_fedex_priority_overnight'), ('freightcom_fedex_standard_overnight', 'freightcom_fedex_standard_overnight'), ('freightcom_fedex_first_overnight', 'freightcom_fedex_first_overnight'), ('freightcom_fedex_international_economy', 'freightcom_fedex_international_economy'), ('freightcom_ups_standard', 'freightcom_ups_standard'), ('freightcom_ups_expedited', 'freightcom_ups_expedited'), ('freightcom_ups_express_saver', 'freightcom_ups_express_saver'), ('freightcom_ups_express', 'freightcom_ups_express'), ('freightcom_ups_express_early', 'freightcom_ups_express_early'), ('freightcom_ups_3_day_select', 'freightcom_ups_3_day_select'), ('freightcom_ups_worldwide_expedited', 'freightcom_ups_worldwide_expedited'), ('freightcom_ups_worldwide_express', 'freightcom_ups_worldwide_express'), ('freightcom_fedex_international_priority', 'freightcom_fedex_international_priority'), ('freightcom_ups_worldwide_express_saver', 'freightcom_ups_worldwide_express_saver'), ('freightcom_purolator_ground_us', 'freightcom_purolator_ground_us'), ('freightcom_purolator_express_us', 'freightcom_purolator_express_us'), ('freightcom_purolator_express_us_10_30_am', 'freightcom_purolator_express_us_10_30_am'), ('freightcom_ups_worldwide_express_plus', 'freightcom_ups_worldwide_express_plus'), ('freightcom_purolator_express_us_9_am', 'freightcom_purolator_express_us_9_am'), ('freightcom_express_easy', 'freightcom_express_easy'), ('freightcom_express_10_30', 'freightcom_express_10_30'), ('freightcom_express_worldwide', 'freightcom_express_worldwide'), ('freightcom_express_12_00', 'freightcom_express_12_00'), ('freightcom_economy_select', 'freightcom_economy_select'), ('freightcom_dayr_e_comm_am_service', 'freightcom_dayr_e_comm_am_service'), ('freightcom_dayr_e_comm_ground_service', 'freightcom_dayr_e_comm_ground_service'), ('freightcom_regular_parcel', 'freightcom_regular_parcel'), ('freightcom_expedited_parcel', 'freightcom_expedited_parcel'), ('freightcom_xpresspost', 'freightcom_xpresspost'), ('freightcom_priority', 'freightcom_priority'), ('eshipper_all', 'eshipper_all'), ('eshipper_fedex_priority', 'eshipper_fedex_priority'), ('eshipper_fedex_first_overnight', 'eshipper_fedex_first_overnight'), ('eshipper_fedex_ground', 'eshipper_fedex_ground'), ('eshipper_fedex_standard_overnight', 'eshipper_fedex_standard_overnight'), ('eshipper_fedex_2nd_day', 'eshipper_fedex_2nd_day'), ('eshipper_fedex_express_saver', 'eshipper_fedex_express_saver'), ('eshipper_fedex_international_economy', 'eshipper_fedex_international_economy'), ('eshipper_purolator_air', 'eshipper_purolator_air'), ('eshipper_purolator_air_9_am', 'eshipper_purolator_air_9_am'), ('eshipper_purolator_air_10_30', 'eshipper_purolator_air_10_30'), ('eshipper_puro_letter', 'eshipper_puro_letter'), ('eshipper_puro_letter_9_am', 'eshipper_puro_letter_9_am'), ('eshipper_puro_letter_10_30', 'eshipper_puro_letter_10_30'), ('eshipper_puro_pak', 'eshipper_puro_pak'), ('eshipper_puro_pak_9_am', 'eshipper_puro_pak_9_am'), ('eshipper_puro_pak_10_30', 'eshipper_puro_pak_10_30'), ('eshipper_purolator_ground', 'eshipper_purolator_ground'), ('eshipper_purolator_ground_9_am', 'eshipper_purolator_ground_9_am'), ('eshipper_purolator_ground_10_30', 'eshipper_purolator_ground_10_30'), ('eshipper_canada_worldwide_same_day', 'eshipper_canada_worldwide_same_day'), ('eshipper_canada_worldwide_next_flight_out', 'eshipper_canada_worldwide_next_flight_out'), ('eshipper_canada_worldwide_air_freight', 'eshipper_canada_worldwide_air_freight'), ('eshipper_canada_worldwide_ltl', 'eshipper_canada_worldwide_ltl'), ('eshipper_dhl_express_worldwide', 'eshipper_dhl_express_worldwide'), ('eshipper_dhl_express_12_pm', 'eshipper_dhl_express_12_pm'), ('eshipper_dhl_express_10_30_am', 'eshipper_dhl_express_10_30_am'), ('eshipper_dhl_esi_export', 'eshipper_dhl_esi_export'), ('eshipper_dhl_international_express', 'eshipper_dhl_international_express'), ('eshipper_ups_express_next_day_air', 'eshipper_ups_express_next_day_air'), ('eshipper_ups_expedited_second_day_air', 'eshipper_ups_expedited_second_day_air'), ('eshipper_ups_worldwide_express', 'eshipper_ups_worldwide_express'), ('eshipper_ups_worldwide_expedited', 'eshipper_ups_worldwide_expedited'), ('eshipper_ups_standard_ground', 'eshipper_ups_standard_ground'), ('eshipper_ups_express_early_am_next_day_air_early_am', 'eshipper_ups_express_early_am_next_day_air_early_am'), ('eshipper_ups_three_day_select', 'eshipper_ups_three_day_select'), ('eshipper_ups_saver', 'eshipper_ups_saver'), ('eshipper_ups_ground', 'eshipper_ups_ground'), ('eshipper_next_day_saver', 'eshipper_next_day_saver'), ('eshipper_worldwide_express_plus', 'eshipper_worldwide_express_plus'), ('eshipper_second_day_air_am', 'eshipper_second_day_air_am'), ('eshipper_canada_post_priority', 'eshipper_canada_post_priority'), ('eshipper_canada_post_xpress_post', 'eshipper_canada_post_xpress_post'), ('eshipper_canada_post_expedited', 'eshipper_canada_post_expedited'), ('eshipper_canada_post_regular', 'eshipper_canada_post_regular'), ('eshipper_canada_post_xpress_post_usa', 'eshipper_canada_post_xpress_post_usa'), ('eshipper_canada_post_xpress_post_intl', 'eshipper_canada_post_xpress_post_intl'), ('eshipper_canada_post_air_parcel_intl', 'eshipper_canada_post_air_parcel_intl'), ('eshipper_canada_post_surface_parcel_intl', 'eshipper_canada_post_surface_parcel_intl'), ('eshipper_canada_post_expedited_parcel_usa', 'eshipper_canada_post_expedited_parcel_usa'), ('eshipper_tst_ltl', 'eshipper_tst_ltl'), ('eshipper_ltl_chicago_suburban_express', 'eshipper_ltl_chicago_suburban_express'), ('eshipper_ltl_fedex_freight_east', 'eshipper_ltl_fedex_freight_east'), ('eshipper_ltl_fedex_freight_west', 'eshipper_ltl_fedex_freight_west'), ('eshipper_ltl_mid_states_express', 'eshipper_ltl_mid_states_express'), ('eshipper_ltl_new_england_motor_freight', 'eshipper_ltl_new_england_motor_freight'), ('eshipper_ltl_new_penn', 'eshipper_ltl_new_penn'), ('eshipper_ltl_oak_harbor', 'eshipper_ltl_oak_harbor'), ('eshipper_ltl_pitt_ohio', 'eshipper_ltl_pitt_ohio'), ('eshipper_ltl_r_l_carriers', 'eshipper_ltl_r_l_carriers'), ('eshipper_ltl_saia', 'eshipper_ltl_saia'), ('eshipper_ltl_usf_reddaway', 'eshipper_ltl_usf_reddaway'), ('eshipper_ltl_vitran_express', 'eshipper_ltl_vitran_express'), ('eshipper_ltl_wilson_trucking', 'eshipper_ltl_wilson_trucking'), ('eshipper_ltl_yellow_transportation', 'eshipper_ltl_yellow_transportation'), ('eshipper_ltl_roadway', 'eshipper_ltl_roadway'), ('eshipper_ltl_fedex_national', 'eshipper_ltl_fedex_national'), ('eshipper_wilson_trucking_tfc', 'eshipper_wilson_trucking_tfc'), ('eshipper_aaa_cooper_transportation', 'eshipper_aaa_cooper_transportation'), ('eshipper_roadrunner_dawes', 'eshipper_roadrunner_dawes'), ('eshipper_new_england_motor_freight', 'eshipper_new_england_motor_freight'), ('eshipper_new_penn_motor_express', 'eshipper_new_penn_motor_express'), ('eshipper_dayton_freight', 'eshipper_dayton_freight'), ('eshipper_southeastern_freightway', 'eshipper_southeastern_freightway'), ('eshipper_saia_inc', 'eshipper_saia_inc'), ('eshipper_conway', 'eshipper_conway'), ('eshipper_roadway', 'eshipper_roadway'), ('eshipper_usf_reddaway', 'eshipper_usf_reddaway'), ('eshipper_usf_holland', 'eshipper_usf_holland'), ('eshipper_dependable_highway_express', 'eshipper_dependable_highway_express'), ('eshipper_day_and_ross', 'eshipper_day_and_ross'), ('eshipper_day_and_ross_r_and_l', 'eshipper_day_and_ross_r_and_l'), ('eshipper_ups', 'eshipper_ups'), ('eshipper_aaa_cooper', 'eshipper_aaa_cooper'), ('eshipper_ama_transportation', 'eshipper_ama_transportation'), ('eshipper_averitt_express', 'eshipper_averitt_express'), ('eshipper_central_freight', 'eshipper_central_freight'), ('eshipper_conway_us', 'eshipper_conway_us'), ('eshipper_dayton', 'eshipper_dayton'), ('eshipper_drug_transport', 'eshipper_drug_transport'), ('eshipper_estes', 'eshipper_estes'), ('eshipper_land_air_express', 'eshipper_land_air_express'), ('eshipper_fedex_west', 'eshipper_fedex_west'), ('eshipper_fedex_national', 'eshipper_fedex_national'), ('eshipper_usf_holland_us', 'eshipper_usf_holland_us'), ('eshipper_lakeville_m_express', 'eshipper_lakeville_m_express'), ('eshipper_milan_express', 'eshipper_milan_express'), ('eshipper_nebraska_transport', 'eshipper_nebraska_transport'), ('eshipper_new_england', 'eshipper_new_england'), ('eshipper_new_penn', 'eshipper_new_penn'), ('eshipper_a_duie_pyle', 'eshipper_a_duie_pyle'), ('eshipper_roadway_us', 'eshipper_roadway_us'), ('eshipper_usf_reddaway_us', 'eshipper_usf_reddaway_us'), ('eshipper_rhody_transportation', 'eshipper_rhody_transportation'), ('eshipper_saia_motor_freight', 'eshipper_saia_motor_freight'), ('eshipper_southeastern_frgt', 'eshipper_southeastern_frgt'), ('eshipper_pitt_ohio', 'eshipper_pitt_ohio'), ('eshipper_ward', 'eshipper_ward'), ('eshipper_wilson', 'eshipper_wilson'), ('eshipper_chi_cargo', 'eshipper_chi_cargo'), ('eshipper_tax_air', 'eshipper_tax_air'), ('eshipper_fedex_east', 'eshipper_fedex_east'), ('eshipper_central_transport', 'eshipper_central_transport'), ('eshipper_roadrunner', 'eshipper_roadrunner'), ('eshipper_r_and_l_carriers', 'eshipper_r_and_l_carriers'), ('eshipper_estes_us', 'eshipper_estes_us'), ('eshipper_yrc_roadway', 'eshipper_yrc_roadway'), ('eshipper_central_transport_us', 'eshipper_central_transport_us'), ('eshipper_absolute_transportation_services', 'eshipper_absolute_transportation_services'), ('eshipper_blue_sky_express', 'eshipper_blue_sky_express'), ('eshipper_galasso_trucking', 'eshipper_galasso_trucking'), ('eshipper_griley_air_freight', 'eshipper_griley_air_freight'), ('eshipper_jet_transportation', 'eshipper_jet_transportation'), ('eshipper_metro_transportation_logistics', 'eshipper_metro_transportation_logistics'), ('eshipper_oak_harbor', 'eshipper_oak_harbor'), ('eshipper_stream_links_express', 'eshipper_stream_links_express'), ('eshipper_tiffany_trucking', 'eshipper_tiffany_trucking'), ('eshipper_ups_freight', 'eshipper_ups_freight'), ('eshipper_roadrunner_us', 'eshipper_roadrunner_us'), ('eshipper_global_mail_parcel_priority', 'eshipper_global_mail_parcel_priority'), ('eshipper_global_mail_parcel_standard', 'eshipper_global_mail_parcel_standard'), ('eshipper_global_mail_packet_plus_priority', 'eshipper_global_mail_packet_plus_priority'), ('eshipper_global_mail_packet_priority', 'eshipper_global_mail_packet_priority'), ('eshipper_global_mail_packet_standard', 'eshipper_global_mail_packet_standard'), ('eshipper_global_mail_business_priority', 'eshipper_global_mail_business_priority'), ('eshipper_global_mail_business_standard', 'eshipper_global_mail_business_standard'), ('eshipper_global_mail_parcel_direct_priority', 'eshipper_global_mail_parcel_direct_priority'), ('eshipper_global_mail_parcel_direct_standard', 'eshipper_global_mail_parcel_direct_standard'), ('eshipper_ground', 'eshipper_ground'), ('eshipper_select_parcel', 'eshipper_select_parcel'), ('eshipper_express_parcel', 'eshipper_express_parcel'), ('dhl_logistics_services', 'dhl_logistics_services'), ('dhl_domestic_express_12_00_doc', 'dhl_domestic_express_12_00_doc'), ('dhl_b2_c_doc', 'dhl_b2_c_doc'), ('dhl_b2_c_nondoc', 'dhl_b2_c_nondoc'), ('dhl_jetline', 'dhl_jetline'), ('dhl_sprintline', 'dhl_sprintline'), ('dhl_express_easy_doc', 'dhl_express_easy_doc'), ('dhl_express_easy_nondoc', 'dhl_express_easy_nondoc'), ('dhl_europack_doc', 'dhl_europack_doc'), ('dhl_auto_reversals', 'dhl_auto_reversals'), ('dhl_breakbulk_express_doc', 'dhl_breakbulk_express_doc'), ('dhl_medical_express_doc', 'dhl_medical_express_doc'), ('dhl_express_worldwide_doc', 'dhl_express_worldwide_doc'), ('dhl_express_9_00_nondoc', 'dhl_express_9_00_nondoc'), ('dhl_freight_worldwide_nondoc', 'dhl_freight_worldwide_nondoc'), ('dhl_domestic_economy_select_doc', 'dhl_domestic_economy_select_doc'), ('dhl_economy_select_nondoc', 'dhl_economy_select_nondoc'), ('dhl_domestic_express_9_00_doc', 'dhl_domestic_express_9_00_doc'), ('dhl_jumbo_box_nondoc', 'dhl_jumbo_box_nondoc'), ('dhl_express_9_00_doc', 'dhl_express_9_00_doc'), ('dhl_express_10_30_doc', 'dhl_express_10_30_doc'), ('dhl_express_10_30_nondoc', 'dhl_express_10_30_nondoc'), ('dhl_domestic_express_doc', 'dhl_domestic_express_doc'), ('dhl_domestic_express_10_30_doc', 'dhl_domestic_express_10_30_doc'), ('dhl_express_worldwide_nondoc', 'dhl_express_worldwide_nondoc'), ('dhl_medical_express_nondoc', 'dhl_medical_express_nondoc'), ('dhl_globalmail_business_doc', 'dhl_globalmail_business_doc'), ('dhl_same_day_doc', 'dhl_same_day_doc'), ('dhl_express_12_00_doc', 'dhl_express_12_00_doc'), ('dhl_europack_nondoc', 'dhl_europack_nondoc'), ('dhl_economy_select_doc', 'dhl_economy_select_doc'), ('dhl_express_envelope_doc', 'dhl_express_envelope_doc'), ('dhl_express_12_00_nondoc', 'dhl_express_12_00_nondoc'), ('dhl_destination_charges', 'dhl_destination_charges')], max_length=100), blank=True, help_text='\n        The list of services you want to apply the surcharge to.\n        Note that by default, the surcharge is applied to all services\n        ', null=True, size=None)),
                ('discount_range', django.contrib.postgres.fields.ranges.DecimalRangeField(blank=True, help_text='\n        Add the surcharge, if the rate discount is within this discount rate range. \n        \n        By default, the surcharge is applied to all quotes no matter the discount amount.\n        ', null=True)),
                ('freight_range', django.contrib.postgres.fields.ranges.DecimalRangeField(blank=True, help_text='\n        Add the surcharge, if the rate charge is within this freight (quote) price range. \n        \n        By default, the surcharge is applied to all quotes no matter the amount.\n        ', null=True)),
            ],
            options={
                'verbose_name': 'Broker Surcharge',
                'verbose_name_plural': 'Broker Surcharges',
                'db_table': 'surcharge',
            },
        ),
        migrations.DeleteModel(
            name='PricingCharge',
        ),
    ]
