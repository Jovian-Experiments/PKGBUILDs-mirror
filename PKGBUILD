# Maintainer: David Runge <dvzrv@archlinux.org>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

# Holo: Enable SCO offload. That patch is coming from https://gitlab.steamos.cloud/holo/holo/-/merge_requests/847,
# but from that MR it is unclear if we need it or if it is upstreamable.
# Related to https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1241
# Holo: The second patch we include is a backport from upstream to fix the Airpods.
# Once we update to a newer pipewire that includes it, we can remove this backport
# Holo: Symlink the `.conf.d` directories of pipewire to `/run/pipewire`. This is required
# by steamdeck-dsp

pkgbase=pipewire
pkgname=(
  pipewire
  libpipewire
  alsa-card-profiles
  pipewire-docs
  pipewire-libcamera
  pipewire-audio
  pipewire-alsa
  pipewire-ffado
  pipewire-jack-client
  pipewire-jack
  pipewire-pulse
  pipewire-roc
  gst-plugin-pipewire
  pipewire-zeroconf
  pipewire-v4l2
  pipewire-x11-bell
  pipewire-session-manager
  pulse-native-provider
)
pkgver=1.4.10
pkgrel=1.3
epoch=1
pkgdesc="Low-latency audio/video router and processor"
url="https://pipewire.org"
arch=(x86_64)
license=(MIT)
makedepends=(
  alsa-lib
  avahi
  bluez-libs
  dbus
  doxygen
  git
  glib2
  glib2-devel
  graphviz
  gst-plugins-base
  jack2
  libcamera
  libcanberra
  libebur128
  libfdk-aac
  libffado
  libfreeaptx
  liblc3
  libldac
  libmysofa
  libpulse
  libsndfile
  libusb
  libx11
  libxfixes
  lilv
  meson
  # Holo: For HFP certification
  modemmanager
  ncurses
  opus
  'python>=3.13'
  'python<3.14'
  python-docutils
  readline
  roc-toolkit
  rtkit
  sbc
  sdl2
  systemd
  valgrind
  webrtc-audio-processing-1
)
checkdepends=(
  desktop-file-utils
  openal
)
source=(
    "git+https://gitlab.freedesktop.org/pipewire/pipewire.git#tag=$pkgver"
    # Holo
    "0001-pipeware-bluez5-backend-native-Enable-SCO-offload.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2422
    # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1675
    "0001-alsa-add-option-to-disable-pro-audio-profiles.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2560
    # First 4 are dependencies, last two are from the MR
    "0001-alsa-Use-the-configured-max-channels.patch"
    "0002-Remove-some-hardcoded-channel-number-values.patch"
    "0003-pulse-clamp-channel-numbers-to-right-values.patch"
    "0004-acp-remove-channel-limit-from-API.patch"
    "0005-spa-alsa-Read-and-expose-channel-count-and-position-.patch"
    "0006-spa-alsa-Add-option-to-use-ELD-detected-channels.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2639
    "0001-spa-alsa-Guard-against-mismatched-LPCM-channel-count.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2642
    "0002-spa-alsa-Fix-off-by-one-check-in-ELD-channel-positio.patch"

    # Holo: Backports for HFP AG qualification
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2604
    "0009-spa-bluez-modemmanager-Fix-NameOwnerChanged.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2605
    "0010-spa-bluez-backend-native-Fix-CNUM-reply.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2606
    "0011-spa-bluez-backend-native-Fix-CIEV-call-status-suppor.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2609
    "0012-spa-bluez-backend-native-Fix-BIEV-HF-indicators-supp.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2617
    "0013-spa-bluez-device-Add-SPA_PROP_params-to-disable-dumm.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2631
    "0014-doc-Add-property-documentation-for-bluez5.disable-du.patch"
    "0015-spa-bluez-modemmanager-Add-support-for-memory-dialin.patch"
    "0016-spa-bluez-backend-native-Add-support-for-AT-BLDN-for.patch"
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2638
    "0017-spa-bluez-backend-native-Fix-audio-connection-policy.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2646
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2674
    "0001-pulse-server-Fix-querying-after-setting-of-mono-mixd.patch"
    "0002-pipewire-pulse-Expose-bluetooth-headset-autoswitch-c.patch"
    "0003-pulse-server-use-null-to-clear-the-value.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2752
    "0001-bluez-Add-A2DP-auto-quality-and-latency-profiles.patch"
)
b2sums=('5c7c50e83200001fbaac5bdb9497eed56e68ebe3be5a75f1cb843d73ef855870f8da09b456b3530a7c66ce6a87665b386c00d4bbffb6c96f88ab9d65ba60c8ae'
        '68ad58cb1a8c532a194b7982167e6b461ff3a2d046f346305c38d3af21a696a2cd18619b73b99cc1b41c55f8786cf26ab5c077f58652e8197a9f5f42416c764f'
        '98bccdbe20da61ffb5d1e81029983bf947ae010198d70eb93851f8ddce72338944829f8d369da73e71ac4d85bd5279d0fdd923dac307516f15bad8c565aa4d92'
        '95427f88ad7d690811c9eca4e9d29fdc6f15ddd8dc64d14d5682749b07765e64552d3a15efe8b350478d32a90499ca2e7820bc1e473cd6cbd26901706995b556'
        '2bb4bd117024c061364bb9cf44a54c7f633b8ea7106c4cc3ee047b3c591a1ac9d1b9c226f43d790b29968eecad7f6883b652a2b5d4460979a791032645ad8ef4'
        '23f5357b5aaba0f8e20e77b641af555004780caae68f77f9ca12d214bec3d7429718afac3512a8310bd49a99fa4b6e67b41faf3038e1e9221416c9d0d5deb1b1'
        '89f8f590134f07b56dd3500265d8195d6bf8e6d6a0d73422bf682f63d8159405362fb85c9057dfc422ce7d1033a0173b26ac26515d46f5c7d32f696204581620'
        '87f723232450d404b1505299005ac8ac6ad01b4278d87771ebc9675a67feb401249db159cf65c1f44ba3ae78ef3bd0d83255be5546d0f06aa8e41ed0b7005a8d'
        'eaf1e55589fbfe28db7e16138425969e2e1016a7ba75fb9af507677009bcbd3414a2d86ea4f644ad5b625b49eb8c33679404390ae8e7702e854bd0adf4801757'
        '148f6315f25fb956fdab4935ceea35f83cae36afdbb1d5471103445f5a7a45fd27cb1921b1926a39d382dead0f2be9842c36b01a62ba566b93331cbf45bf38b0'
        '57aafc323d58e38b781528e21ac5f642fd7de11ad153ff12093e4d1807a1768fe38c40cde8902b888908a8c6484ccf3affe52ac9f2274064bfd50114bae96f5b'
        'fd2bfdd8601b142e9812058613bb69066c1e852145b0543ad8705a8415cd24c92e107f8420db6215f9723059fe2acc38825e4f4b4b5acaf9cbda32007aa13cf6'
        '47d91be7e62f3bab9725ddd1f62ff075619f27e52e90b1b7586a08704067f277ead95affcc2945ba48f9830ed6d95cf001df1c3af21ac7dbe858e578047d65b3'
        '76366abab04dc24df31d3943b0a28113bfdae54f8f8fec1fd8e8248a45779992b29e8c4870ce3aaf3fcadee0f46e50220bf7afdd93f964d3509811df39815667'
        '17e52ec774230f6a88de11ef334b5937644e263f8616ac6302eb8ea4c6b5f55593255cd95489cee41c6957b88bf0b69ae050616f9635207d02969d5c867328ff'
        '9f6ad262db5ac5dce91bf16bb1956f41f4d86c2f80844c2b1ebba119054c3d002bed9ec436a71ee616719aa2428c6a02fb70b4d1074ea1cc66552bc9a1facfec'
        'c5f75947e36c72496e5c567d471c5fc7f62ea7e7f932a15c14118883bc39f79f4415282142587ff577fa7cf3e9d0938f0d560acac28e639c43c8d0daf9221157'
        '7c6b745dd09b60e983db422148cef77ef4cf355d050f4a154959b9c95de786eabfa8970a734b67d548aa08e673662264c556736df64b1d7a887ecbbeb599e53b'
        '9c95db232c9619d417fb0441943ec815df3b6d9a5043082854d295e020f315fc0c83ce8f6af3e0e8c9e946e80ed86df174eafddd72f38d423408afccd4cdcc57'
        '2c97fa28a82d0f725ff169698edfad53cdb4d3131e79adbb1e7cd896ce96b4cb566bb5ae40d47e56775e61bd533d270c34af38db9f93c1b8e414f1eca445c3b4'
        '257adcde47c4eb618f86d8d16c479ca56057bc88fb44f5539b00ab4278fbe8d74d0ec820acff8e986f6df6c63076f0541c52ad931fd2bde8ee1da5dc79915b02'
        '5910c022a8604edea4629d5f9250c984c6f7b21c24b90e12e57ca0329fa85a8c2249c77f9ed7dd0defd8c99f8e583ff28aa91a22fd2522bde7212ab11f616b91'
        '17f420873f14f67b86b9521dd8e34b1cadad3dd2d2ba790e92a3bbda49593e33436fa8fcfa6ab3c4d873793beab9fcd032de6aca0baf7b9c1ec3a3df6045bce5'
        'd386030c992eb6dc874706cde1b743dca4470246065aa0c3692808614ba3b1f3664876c34d6e67c5505efcee7ca9936af057798a9b67f922e9470e012e86dd2a')

prepare() {
  cd pipewire

  # Holo: apply downstream patches
  local src
  for src in "${source[@]}"; do
    [[ $src = *.patch ]] || continue
    src="${src##*/}"
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done
}

build() {
  local meson_options=(
    # Holo: Enable for HFP certification
    -D bluez5-backend-native-mm=enabled
    -D bluez5-codec-lc3plus=disabled
    -D docs=enabled
    -D jack-devel=true
    -D libjack-path=/usr/lib
    -D man=enabled
    -D rlimits-install=false
    -D selinux=disabled
    -D session-managers=[]
    -D snap=disabled
    -D udevrulesdir=/usr/lib/udev/rules.d
  )

  arch-meson pipewire build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

_pwname=pipewire-0.3
_spaname=spa-0.2

package_pipewire() {
  license+=(
    # libspa-alsa
    LGPL-2.1-or-later
  )
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    dbus libdbus-1.so
    gcc-libs
    glib2 libglib-2.0.so
    glibc
    ncurses libncursesw.so
    readline libreadline.so
    systemd-libs libsystemd.so libudev.so
    # Holo: required to handle the /run/pipewire symlinks
    'steamdeck-dsp>=0.43'
  )
  optdepends=(
    'gst-plugin-pipewire: GStreamer plugin'
    'pipewire-alsa: ALSA configuration'
    'pipewire-audio: Audio support'
    'pipewire-docs: Documentation'
    'pipewire-ffado: FireWire support'
    'pipewire-jack-client: PipeWire as JACK client'
    'pipewire-jack: JACK replacement'
    'pipewire-libcamera: Libcamera support'
    'pipewire-pulse: PulseAudio replacement'
    'pipewire-roc: ROC streaming'
    'pipewire-session-manager: Session manager'
    'pipewire-v4l2: V4L2 interceptor'
    'pipewire-x11-bell: X11 bell'
    'pipewire-zeroconf: Zeroconf support'
    'realtime-privileges: realtime privileges with rt module'
    'rtkit: realtime privileges with rtkit module'
  )
  install=pipewire.install

  meson install -C build --destdir "$pkgdir"

  (
    cd "$pkgdir"

    # Replace copies with symlinks
    for _f in pipewire-{aes67,avb,pulse}; do
      cmp usr/bin/pipewire usr/bin/$_f
      ln -sf pipewire usr/bin/$_f
    done

    _pick lib usr/include/{$_pwname,$_spaname}
    _pick lib usr/lib/$_spaname/libspa.so*
    _pick lib usr/lib/lib$_pwname.so*
    _pick lib usr/lib/pkgconfig/lib{$_pwname,$_spaname}.pc

    _pick acp usr/lib/udev
    _pick acp usr/share/alsa-card-profile

    _pick docs usr/share/doc

    _pick libcamera usr/lib/$_spaname/libcamera

    _pick audio usr/bin/pipewire-{aes67,avb}
    _pick audio usr/bin/pw-{cat,loopback,mididump}
    _pick audio usr/bin/pw-{dsd,enc,midi,}play
    _pick audio usr/bin/pw-{midi,}record
    _pick audio usr/bin/spa-{acp-tool,resample}
    _pick audio usr/lib/alsa-lib
    _pick audio usr/lib/$_pwname/libpipewire-module-avb.so
    _pick audio usr/lib/$_pwname/libpipewire-module-echo-cancel.so
    _pick audio usr/lib/$_pwname/libpipewire-module-fallback-sink.so
    _pick audio usr/lib/$_pwname/libpipewire-module-filter-chain*.so
    _pick audio usr/lib/$_pwname/libpipewire-module-loopback.so
    _pick audio usr/lib/$_pwname/libpipewire-module-netjack2*.so
    _pick audio usr/lib/$_pwname/libpipewire-module-parametric-equalizer.so
    _pick audio usr/lib/$_pwname/libpipewire-module-pipe-tunnel.so
    _pick audio usr/lib/$_pwname/libpipewire-module-protocol-simple.so
    _pick audio usr/lib/$_pwname/libpipewire-module-rtp-{sap,sink,source}.so
    _pick audio usr/lib/$_pwname/libpipewire-module-vban*.so
    _pick audio usr/lib/$_spaname/{aec,alsa,audio*,avb,bluez5,filter-graph}
    _pick audio usr/lib/systemd/user/filter-chain.service
    _pick audio usr/share/alsa
    _pick audio usr/share/man/man1/pw-{cat,loopback,mididump}.1
    _pick audio usr/share/man/man1/spa-{acp-tool,resample}.1
    _pick audio usr/share/man/man5/pipewire-filter-chain.conf.5
    _pick audio usr/share/man/man7/libpipewire-module-avb.7
    _pick audio usr/share/man/man7/libpipewire-module-echo-cancel.7
    _pick audio usr/share/man/man7/libpipewire-module-fallback-sink.7
    _pick audio usr/share/man/man7/libpipewire-module-filter-chain*.7
    _pick audio usr/share/man/man7/libpipewire-module-loopback.7
    _pick audio usr/share/man/man7/libpipewire-module-netjack2*.7
    _pick audio usr/share/man/man7/libpipewire-module-parametric-equalizer.7
    _pick audio usr/share/man/man7/libpipewire-module-pipe-tunnel.7
    _pick audio usr/share/man/man7/libpipewire-module-protocol-simple.7
    _pick audio usr/share/man/man7/libpipewire-module-rtp-{sap,sink,source}.7
    _pick audio usr/share/man/man7/libpipewire-module-vban*.7
    _pick audio usr/share/pipewire/filter-chain*
    _pick audio usr/share/pipewire/pipewire-{aes67,avb}.conf
    _pick audio usr/share/$_spaname/bluez5

    _pick ffado usr/lib/$_pwname/libpipewire-module-ffado*.so
    _pick ffado usr/share/man/man7/libpipewire-module-ffado-driver.7

    _pick jack-client usr/lib/$_pwname/libpipewire-module-jack{-tunnel,dbus-detect}.so
    _pick jack-client usr/lib/$_spaname/jack
    _pick jack-client usr/share/man/man7/libpipewire-module-jack{-tunnel,dbus-detect}.7

    _pick jack usr/bin/pw-jack
    _pick jack usr/include/jack
    _pick jack usr/lib/libjack*
    _pick jack usr/lib/pkgconfig/jack*.pc
    _pick jack usr/share/man/man1/pw-jack.1
    _pick jack usr/share/man/man5/pipewire-jack.conf.5
    _pick jack usr/share/pipewire/jack.conf

    _pick pulse usr/bin/pipewire-pulse
    _pick pulse usr/lib/$_pwname/libpipewire-module-protocol-pulse.so
    _pick pulse usr/lib/$_pwname/libpipewire-module-pulse-tunnel.so
    _pick pulse usr/lib/systemd/user/pipewire-pulse.*
    _pick pulse usr/share/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml
    _pick pulse usr/share/man/man1/pipewire-pulse.1
    _pick pulse usr/share/man/man5/pipewire-pulse.conf.5
    _pick pulse usr/share/man/man7/libpipewire-module-{protocol-pulse,pulse-tunnel}.7
    _pick pulse usr/share/man/man7/pipewire-pulse*.7
    _pick pulse usr/share/pipewire/pipewire-pulse.conf

    _pick roc usr/lib/$_pwname/libpipewire-module-roc*.so
    _pick roc usr/share/man/man7/libpipewire-module-roc-{sink,source}.7

    _pick gst usr/lib/gstreamer-1.0

    _pick zeroconf usr/lib/$_pwname/libpipewire-module-{raop,zeroconf}-*.so
    _pick zeroconf usr/lib/$_pwname/libpipewire-module-rtp-session.so
    _pick zeroconf usr/lib/$_pwname/libpipewire-module-snapcast-discover.so
    _pick zeroconf usr/share/man/man7/libpipewire-module-{raop,zeroconf}-*.7
    _pick zeroconf usr/share/man/man7/libpipewire-module-rtp-session.7
    _pick zeroconf usr/share/man/man7/libpipewire-module-snapcast-discover.7

    _pick v4l2 usr/bin/pw-v4l2 usr/lib/$_pwname/v4l2
    _pick v4l2 usr/share/man/man1/pw-v4l2.1

    _pick x11-bell usr/lib/$_pwname/libpipewire-module-x11-bell.so
    _pick x11-bell usr/share/man/man7/libpipewire-module-x11-bell.7

    # Holo: we symlink the .conf.d directories from /etc/pipewire to /run because at
    # runtime the script pipewire-hwconfig picks up the correct config files based
    # on the hw.
    # TODO: this change needs to happen outside the pipewire package to allow us to
    # reconcile with the upstream PKGBUILD. Alternatively we need to figure out a
    # better way to handle hw specific configs that doesn't involve symlinks in /run
    mkdir -p etc/pipewire
    for _l in {client-rt,client,filter-chain,minimal,pipewire}.conf.d
    do
      ln -s /run/pipewire/${_l} etc/pipewire/${_l}
    done
  )

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_libpipewire() {
  pkgdesc+=" - client library"
  depends=(
    glibc
    gcc-libs
  )
  provides=(lib$_pwname.so)

  mv lib/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_alsa-card-profiles() {
  pkgdesc+=" - ALSA card profiles"
  license=(LGPL-2.1-or-later)

  mv acp/* "$pkgdir"
}

package_pipewire-docs() {
  pkgdesc+=" - documentation"

  mv docs/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-libcamera() {
  pkgdesc+=" - Libcamera support"
  depends=(
    gcc-libs
    glibc
    libcamera libcamera-base.so libcamera.so
    pipewire
  )

  mv libcamera/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-audio() {
  pkgdesc+=" - Audio support"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire=$epoch:$pkgver-$pkgrel"
    alsa-card-profiles
    alsa-lib libasound.so
    bluez-libs libbluetooth.so
    dbus libdbus-1.so
    gcc-libs
    glib2 libg{lib,object,io}-2.0.so
    glibc
    libebur128
    libfdk-aac libfdk-aac.so
    libfreeaptx libfreeaptx.so
    liblc3 liblc3.so
    libldac libldacBT_enc.so
    libmysofa libmysofa.so
    libsndfile libsndfile.so
    libusb libusb-1.0.so
    lilv liblilv-0.so
    opus libopus.so
    sbc libsbc.so
    systemd-libs
    webrtc-audio-processing-1 libwebrtc-audio-processing-1.so
  )

  mv audio/* "$pkgdir"

  mkdir -p "$pkgdir/etc/alsa/conf.d"
  ln -st "$pkgdir/etc/alsa/conf.d" \
    /usr/share/alsa/alsa.conf.d/50-pipewire.conf

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-alsa() {
  pkgdesc+=" - ALSA configuration"
  depends=(
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    pipewire-session-manager
  )

  mkdir -p "$pkgdir/etc/alsa/conf.d"
  ln -st "$pkgdir/etc/alsa/conf.d" \
    /usr/share/alsa/alsa.conf.d/99-pipewire-default.conf

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-alsa"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-ffado() {
  pkgdesc+=" - FireWire support"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    glibc
    libffado libffado.so
  )

  mv ffado/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-jack-client() {
  pkgdesc+=" - PipeWire as JACK client"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    dbus libdbus-1.so
    gcc-libs
    glibc
    jack libjack.so
  )
  conflicts=(pipewire-jack)

  mv jack-client/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-jack() {
  pkgdesc+=" - JACK replacement"
  license+=(
    # libjackserver
    GPL-2.0-only
    LGPL-2.1-or-later
  )
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    glibc
    pipewire-session-manager
    sh
    # Holo: required to handle the /run/pipewire symlinks
    'steamdeck-dsp>=0.43'
  )
  optdepends=(
    'jack-example-tools: for official JACK example-clients and tools'
  )
  conflicts=(
    jack
    jack2
    pipewire-jack-client
  )
  provides=(
    jack
    libjack.so
    libjacknet.so
    libjackserver.so
  )

  mv jack/* "$pkgdir"

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-jack"

  # Holo: we symlink the jack.conf.d directory from /etc/pipewire to /run because at
  # runtime the script pipewire-hwconfig picks up the correct config files based
  # on the hw.
  mkdir -p "$pkgdir/etc/pipewire"
  ln -s /run/pipewire/jack.conf.d "$pkgdir"/etc/pipewire/jack.conf.d

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-pulse() {
  pkgdesc+=" - PulseAudio replacement"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    avahi libavahi-{client,common}.so
    dbus libdbus-1.so
    dconf
    gcc-libs
    glib2 libg{lib,object,io}-2.0.so
    glibc
    libpulse libpulse.so
    pipewire-session-manager
    systemd-libs libsystemd.so
    # Holo: required to handle the /run/pipewire symlinks
    'steamdeck-dsp>=0.43'
  )
  provides=(pulse-native-provider)
  conflicts=(pulseaudio)
  install=pipewire-pulse.install

  mv pulse/* "$pkgdir"

  # Holo: we symlink the pipewire-pulse.conf.d directory from /etc/pipewire to /run
  # because at runtime the script pipewire-hwconfig picks up the correct config files
  # based on the hw.
  mkdir -p "$pkgdir/etc/pipewire"
  ln -s /run/pipewire/pipewire-pulse.conf.d \
     "$pkgdir/etc/pipewire/pipewire-pulse.conf.d"

  install -Dm644 /dev/null \
    "$pkgdir/usr/share/pipewire/media-session.d/with-pulseaudio"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-roc() {
  pkgdesc+=" - ROC streaming support"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    gcc-libs
    glibc
    roc-toolkit libroc.so
  )

  mv roc/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_gst-plugin-pipewire() {
  pkgdesc="Multimedia graph framework - pipewire plugin"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    gcc-libs
    glib2 libg{lib,object}-2.0.so
    glibc
    gst-plugins-base-libs
    gstreamer
    pipewire-session-manager
  )

  mv gst/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-zeroconf() {
  pkgdesc+=" - Zeroconf support"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    avahi libavahi-{client,common}.so
    gcc-libs
    glibc
    openssl libcrypto.so
    opus libopus.so
  )

  mv zeroconf/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-v4l2() {
  pkgdesc+=" - V4L2 interceptor"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire=$epoch:$pkgver-$pkgrel"
    glibc
    pipewire-session-manager
    sh
  )

  mv v4l2/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-x11-bell() {
  pkgdesc+=" - X11 bell"
  depends=(
    "libpipewire=$epoch:$pkgver-$pkgrel" lib$_pwname.so
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    glibc
    libcanberra libcanberra.so
    libx11
    libxfixes
  )

  mv x11-bell/* "$pkgdir"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING
}

package_pipewire-session-manager() {
  pkgdesc="Session manager for PipeWire (default provider)"
  license=(CC0-1.0)
  depends=(wireplumber)
}

package_pulse-native-provider() {
  pkgdesc="PulseAudio sound server (default provider)"
  license=(CC0-1.0)
  depends=(pipewire-pulse)
}

# vim:set sw=2 sts=-1 et:
