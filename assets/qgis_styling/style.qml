<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.22.0-Białowieża" maxScale="0" styleCategories="AllStyleCategories" minScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <Option type="Map">
      <Option name="WMSBackgroundLayer" type="bool" value="false"/>
      <Option name="WMSPublishDataSourceUrl" type="bool" value="false"/>
      <Option name="embeddedWidgets/count" type="int" value="0"/>
      <Option name="identify/format" type="QString" value="Value"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option name="name" type="QString" value=""/>
      <Option name="properties"/>
      <Option name="type" type="QString" value="collection"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" enabled="false"/>
    </provider>
    <rasterrenderer alphaBand="-1" opacity="1" classificationMin="4.181519" nodataColor="" band="1" type="singlebandpseudocolor" classificationMax="6.1788898">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>MinMax</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="2" labelPrecision="4" maximumValue="6.1788898000000003" minimumValue="4.1815189999999998" colorRampType="INTERPOLATED" clip="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" type="QString" value="43,131,186,255"/>
              <Option name="color2" type="QString" value="215,25,28,255"/>
              <Option name="discrete" type="QString" value="0"/>
              <Option name="rampType" type="QString" value="gradient"/>
              <Option name="stops" type="QString" value="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255"/>
            </Option>
            <prop k="color1" v="43,131,186,255"/>
            <prop k="color2" v="215,25,28,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255"/>
          </colorramp>
          <item color="#2b83ba" label="4.1815" value="4.181519031524658" alpha="255"/>
          <item color="#4092b6" label="4.2647" value="4.264742811520894" alpha="255"/>
          <item color="#56a1b3" label="4.3480" value="4.347966591517131" alpha="255"/>
          <item color="#6bb0af" label="4.4312" value="4.431190371513367" alpha="255"/>
          <item color="#80bfab" label="4.5144" value="4.514414151509603" alpha="255"/>
          <item color="#96cea8" label="4.5976" value="4.59763793150584" alpha="255"/>
          <item color="#abdda4" label="4.6809" value="4.680861711502075" alpha="255"/>
          <item color="#b9e3a9" label="4.7641" value="4.764085491498311" alpha="255"/>
          <item color="#c7e8ad" label="4.8473" value="4.847309271494548" alpha="255"/>
          <item color="#d5eeb2" label="4.9305" value="4.930533051490784" alpha="255"/>
          <item color="#e3f4b6" label="5.0138" value="5.01375683148702" alpha="255"/>
          <item color="#f1f9bb" label="5.0970" value="5.096980611483256" alpha="255"/>
          <item color="#ffffbf" label="5.1802" value="5.180204391479492" alpha="255"/>
          <item color="#fff2af" label="5.2634" value="5.263428171475728" alpha="255"/>
          <item color="#fee4a0" label="5.3467" value="5.346651951471964" alpha="255"/>
          <item color="#fed790" label="5.4299" value="5.429875731468201" alpha="255"/>
          <item color="#fec980" label="5.5131" value="5.513099511464437" alpha="255"/>
          <item color="#fdbb71" label="5.5963" value="5.596323291460672" alpha="255"/>
          <item color="#fdae61" label="5.6795" value="5.67954707145691" alpha="255"/>
          <item color="#f79556" label="5.7628" value="5.762770851453145" alpha="255"/>
          <item color="#f07c4a" label="5.8460" value="5.845994631449381" alpha="255"/>
          <item color="#ea643f" label="5.9292" value="5.929218411445618" alpha="255"/>
          <item color="#e44b33" label="6.0124" value="6.012442191441854" alpha="255"/>
          <item color="#dd3227" label="6.0957" value="6.09566597143809" alpha="255"/>
          <item color="#d7191c" label="6.1789" value="6.178889751434326" alpha="255"/>
          <rampLegendSettings suffix="" minimumLabel="" useContinuousLegend="1" maximumLabel="" direction="0" orientation="2" prefix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="QChar" value=""/>
                <Option name="decimals" type="int" value="6"/>
                <Option name="rounding_type" type="int" value="0"/>
                <Option name="show_plus" type="bool" value="false"/>
                <Option name="show_thousand_separator" type="bool" value="true"/>
                <Option name="show_trailing_zeros" type="bool" value="false"/>
                <Option name="thousand_separator" type="QChar" value=""/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast gamma="1" contrast="0" brightness="0"/>
    <huesaturation colorizeBlue="128" colorizeStrength="100" grayscaleMode="0" invertColors="0" saturation="0" colorizeRed="255" colorizeGreen="128" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
