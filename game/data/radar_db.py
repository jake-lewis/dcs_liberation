from dcs.ships import (
    Forrestal,
    PIOTR,
    MOSCOW,
    VINSON,
    CVN_71,
    CVN_72,
    CVN_73,
    Stennis,
    KUZNECOW,
    CV_1143_5,
    NEUSTRASH,
    ALBATROS,
    REZKY,
    MOLNIYA,
    LHA_Tarawa,
    PERRY,
    TICONDEROG,
    Type_052B,
    Type_052C,
    Type_054A,
    USS_Arleigh_Burke_IIa,
)
from dcs.vehicles import AirDefence
from pydcs_extensions import highdigitsams as hds

TELARS = {
    AirDefence._2S6_Tunguska,
    AirDefence.SA_11_Buk_LN_9A310M1,
    AirDefence.Osa_9A33_ln,
    AirDefence.Tor_9A331,
    AirDefence.Roland_ADS,
    hds.SAM_SA_17_Buk_M1_2_LN_9A310M1_2,
}

TRACK_RADARS = {
    AirDefence.Kub_1S91_str,
    AirDefence.Snr_s_125_tr,
    AirDefence.S_300PS_40B6M_tr,
    AirDefence.Hawk_tr,
    AirDefence.Patriot_str,
    AirDefence.SNR_75V,
    AirDefence.RPC_5N62V,
    AirDefence.Rapier_fsa_blindfire_radar,
    AirDefence.HQ_7_STR_SP,
    AirDefence.NASAMS_Radar_MPQ64F1,
    hds.SAM_SA_10B_S_300PS_30N6_TR,
    hds.SAM_SA_12_S_300V_9S32_TR,
    hds.SAM_SA_20_S_300PMU1_TR_30N6E,
    hds.SAM_SA_20B_S_300PMU2_TR_92H6E_truck,
    hds.SAM_SA_23_S_300VM_9S32ME_TR,
}

LAUNCHER_TRACKER_PAIRS = {
    AirDefence.Kub_2P25_ln: AirDefence.Kub_1S91_str,
    AirDefence._5p73_s_125_ln: AirDefence.Snr_s_125_tr,
    AirDefence.S_300PS_5P85C_ln: AirDefence.S_300PS_40B6M_tr,
    AirDefence.S_300PS_5P85D_ln: AirDefence.S_300PS_40B6M_tr,
    AirDefence.Hawk_ln: AirDefence.Hawk_tr,
    AirDefence.Patriot_ln: AirDefence.Patriot_str,
    AirDefence.S_75M_Volhov: AirDefence.SNR_75V,
    AirDefence.Rapier_fsa_launcher: AirDefence.Rapier_fsa_blindfire_radar,
    AirDefence.HQ_7_LN_SP: AirDefence.HQ_7_STR_SP,
    AirDefence.S_200_Launcher: AirDefence.RPC_5N62V,
    AirDefence.NASAMS_LN_B: AirDefence.NASAMS_Radar_MPQ64F1,
    AirDefence.NASAMS_LN_C: AirDefence.NASAMS_Radar_MPQ64F1,
    hds.SAM_SA_2__V759__LN_SM_90: AirDefence.SNR_75V,
    hds.SAM_HQ_2_LN_SM_90: AirDefence.SNR_75V,
    hds.SAM_SA_3__V_601P__LN_5P73: AirDefence.Snr_s_125_tr,
    hds.SAM_SA_10B_S_300PS_5P85SE_LN: hds.SAM_SA_10B_S_300PS_30N6_TR,
    hds.SAM_SA_10B_S_300PS_5P85SU_LN: hds.SAM_SA_10B_S_300PS_30N6_TR,
    hds.SAM_SA_12_S_300V_9A82_LN: hds.SAM_SA_12_S_300V_9S32_TR,
    hds.SAM_SA_12_S_300V_9A83_LN: hds.SAM_SA_12_S_300V_9S32_TR,
    hds.SAM_SA_20_S_300PMU1_LN_5P85CE: hds.SAM_SA_20_S_300PMU1_TR_30N6E,
    hds.SAM_SA_20_S_300PMU1_LN_5P85DE: hds.SAM_SA_20_S_300PMU1_TR_30N6E,
    hds.SAM_SA_20B_S_300PMU2_LN_5P85SE2: hds.SAM_SA_20B_S_300PMU2_TR_92H6E_truck,
    hds.SAM_SA_23_S_300VM_9A82ME_LN: hds.SAM_SA_23_S_300VM_9S32ME_TR,
    hds.SAM_SA_23_S_300VM_9A83ME_LN: hds.SAM_SA_23_S_300VM_9S32ME_TR,
}

UNITS_WITH_RADAR = {
    # Radars
    AirDefence._2S6_Tunguska,
    AirDefence.SA_11_Buk_LN_9A310M1,
    AirDefence.Osa_9A33_ln,
    AirDefence.Tor_9A331,
    AirDefence.Gepard,
    AirDefence.Vulcan,
    AirDefence.Roland_ADS,
    AirDefence.ZSU_23_4_Shilka,
    AirDefence._1L13_EWR,
    AirDefence.Kub_1S91_str,
    AirDefence.S_300PS_40B6M_tr,
    AirDefence.S_300PS_40B6MD_sr,
    AirDefence._55G6_EWR,
    AirDefence.S_300PS_64H6E_sr,
    AirDefence.SA_11_Buk_SR_9S18M1,
    AirDefence.Dog_Ear_radar,
    AirDefence.Hawk_tr,
    AirDefence.Hawk_sr,
    AirDefence.Patriot_str,
    AirDefence.Hawk_cwar,
    AirDefence.P_19_s_125_sr,
    AirDefence.Roland_Radar,
    AirDefence.Snr_s_125_tr,
    AirDefence.SNR_75V,
    AirDefence.RLS_19J6,
    AirDefence.RPC_5N62V,
    AirDefence.Rapier_fsa_blindfire_radar,
    AirDefence.HQ_7_LN_SP,
    AirDefence.HQ_7_STR_SP,
    AirDefence.FuMG_401,
    AirDefence.FuSe_65,
    # Ships
    ALBATROS,
    CVN_71,
    CVN_72,
    CVN_73,
    CV_1143_5,
    Forrestal,
    KUZNECOW,
    LHA_Tarawa,
    MOLNIYA,
    MOSCOW,
    NEUSTRASH,
    PERRY,
    PIOTR,
    REZKY,
    Stennis,
    TICONDEROG,
    Type_052B,
    Type_052C,
    Type_054A,
    USS_Arleigh_Burke_IIa,
    VINSON,
}
