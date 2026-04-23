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
  pipewire-onnx
  pipewire-pulse
  pipewire-roc
  gst-plugin-pipewire
  pipewire-zeroconf
  pipewire-v4l2
  pipewire-x11-bell
  pipewire-session-manager
  pulse-native-provider
)
pkgver=1.6.4
pkgrel=1.1
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
  fftw
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
  onnxruntime
  opus
  'python>=3.13'
  'python<3.14'
  python-docutils
  readline
  roc-toolkit
  rtkit
  sbc
  sdl2
  spandsp
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
    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2752
    "0001-bluez-Add-A2DP-auto-quality-and-latency-profiles.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2759
    "0001-bluez-Increase-priority-of-A2DP-quality-and-latency-.patch"
    "0002-bluez-Set-initial-profile-to-quality-A2DP.patch"
    "0003-bluez-Discard-latency-and-quality-codecs-worse-than-.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2722
    "0001-spa-add-a-new-json-builder-helper.patch"
    "0002-json-builder-add-raw-mode-that-leaves-keys-strings-l.patch"
    "0003-json-builder-avoid-indent-on-the-first-item.patch"
    "0004-json-builder-zero-the-struct.patch"
    "0005-json-builder-handle-allocation-failures-in-vasprintf.patch"
    "0006-json-builder-do-better-json-number-check.patch"
    "0007-spa-dbus-Minor-fix-for-incorrect-documentation.patch"
    "0008-spa-Add-a-varlink-client-support-library.patch"
    "0009-spa-Add-a-param-for-audio-volume-control-flags.patch"
    "0010-alsa-Add-a-varlink-interface-definition-for-external.patch"
    "0011-spa-alsa-Add-a-mechanism-for-external-volume-control.patch"
    "0012-spa-device-Add-a-send_command-method.patch"
    "0013-pipewire-device-Add-a-send_command-method.patch"
    "0014-spa-device-Commands-for-external-volume-control.patch"
    "0015-spa-alsa-Support-volume-control-commands-for-externa.patch"
    "0016-pulse-server-Surface-volume-control-flags-as-propert.patch"
    "0017-pulse-server-Expose-commands-for-sink-volume-control.patch")
b2sums=('054c756beae00a1dc9b757864633f9698a8f6cf5c7c187b2f0d0cb762eec74990e3403e949684b24a5e67d499c9257a91fbd7ebbe764ee34fd02f92844419427'
        'b999796fc69ecd661b7cd761b98daf81412e4a02e649d74d8d8ec7d2c6cf0169f6062ea03131313a5b03a50529e956289baf0068f0631ea58243d42f1fae4d6e'
        'ba33b056d13739e24b7e6c46bf9268357eea5a989f8af5021c737978a9a0bd9fb9882cc7e2c6eb8477d7c1e50684c3083ea33123f29a949e600ee1849cfe5cdf'
        '2708c004cbfccc56b6342785f117f2f2ec16aba474df96acf4c9d028462b4c0b8f443f13f387465e24eb628f797615c58e91b53672e01729d18b46da72686d93'
        '23b4ff805917e71741672b5fd2efcccbd9ba65504f3ed776960c70742a29ee8b1c2ec0ba8c068792b949e58da59cc9978ad5b02fe9aa7f6074848c765cc8e906'
        '7e0017bc79a7a852140e8710ad3bdd0d6c72e5b175a6103dd1c8d4952774e7ba20f42b1edd9e69ab3ff42f13be016f9844bffcad327bc6c6379bbad242a5d5a4'
        '07edc2b29f9e7e8a7bf626112491688c07d2aa8cbc4e9434c67216859538cf537762a34bf7b1cf34453ea3f78435a51c45b467af8d23caf4a2802a86fcedf6d7'
        'c12144b97ea833c39b76b27f0f9eef486ac25e5683603dcb976106e0962206f20537283d3ad81cd6baf68e52975ac6583bef93cb2dc15ddb152bb564fa4fb617'
        '748cd41a2d971acf834c94460054324cdac8523576204a624346288f6e4397da3cd8eea72b0cc34f921c8e963b9f229f966307d452dfdde816429512acc0761b'
        '88fcf89e5ae2132e16d15973d7af74a343122a813d52ab3912594a1f57935edba44748ce8dd08546f01b8ae2d8e961ddafc95fdd6efc84ad7ffe56be35cf31a6'
        '3b927d315ce16b4eb5a1fa0a4de976bbe5b7c9686c6fd4cb73c7086d5f6298c1d8c472db52767c377bc8a96d3b16e4dd8007b661882a2c6da1c30c98cff0e66d'
        '2df5613411e79e086ab4abb18ea17c3758cca24b9a16e0ecf4c9c7a01536bdbd4b1664403dd020f42930405cb6be74f838bc2965e3fdb6d93b41d43f96966b18'
        'e745c8e3cc52120f91e4bccfae30f25741025faf1acbf36eae2da59f2866281b3129e6d3cfedf24086bf72fcc08d301d40956cc54b10d50f9c946ef282f440d1'
        '7323bd24802a954d8bdff8d8d434d47e79f10db6197752d6f28a1b66e27bd2240acb53a4d42c81f66b69dfa3a07688bf3fce9e210e2cad49ef04860f8b8236fa'
        'd4017423357d63d0e316cb2efb072a5af46b4bb93bc3dbc9f6b4dbddcb34fe9f070a082785ecbdda00662d0f3b54f31b91289d7ac58189f404233a9472f8c26a'
        'ab9be739cb37345f53c5abe0915fe020e1fac97392a975cd4ef17445caf45172a96403fcc16ef4d46da907a797751441797baaae04f21d728a080fced0392c58'
        'fc73bca74c2f7bc48a9854d5f691409aaffc28e94ca94d95d9d13ee0fee3b17c6cdaf40843277041177c701067c70c72cd27da3e4e85840c03d34d858f7a1e05'
        '573fc501a8b8f432d1f79fff502181e72f7f24569ff6a70208c4b43015b9e3f8977801f5b65cccfb9c4476e4e44b38162ec79389e103c8006e6519aa32e802d1'
        '78f4aef18b74550b4695c6c1a6bd76ba3037f769f1efff1c4bfd4859d2368a552a20bf239f6516ea06835c8c8f3b3d55b3aa1ac52ada27c02d4c009f4e8c4ff0'
        '0ff89a9b49626da19b235067669b5fd1d8e9f7f1ec09783ba28a3d873edef54dae0aba65adf49eacf0b72bc90caee9538995476bad4d0f3cb9e89a96a09c5fed'
        '5f6d26da50dadaf406acc3ab423b4d6c06d5996cda6db88b7befdedca9dfcbe751727cb4a2466e5c6e60b4c7c005b6b9490c4e51117814e34dc201e0fb1e53d1'
        'd3fb1483429d7e29cb4a383c59e08dc39e95a04cfefcf49b4e4966d35545f0a869700749684f3f6672fc41779d83530f794eb0d0e1548634a560616408bf9eaa')

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
    -D bluez5-codec-ldac-dec=disabled
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
    'pipewire-onnx: ONNX filter support'
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

    _pick onnx usr/lib/$_spaname/filter-graph/libspa-filter-graph-plugin-onnx.so

    _pick audio usr/bin/pipewire-{aes67,avb}
    _pick audio usr/bin/pw-{cat,loopback,mididump,midi2play,midi2record,sysex}
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

    # directories for overrides
    mkdir -p etc/pipewire/{client-rt,client,minimal,pipewire}.conf.d

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
    fftw libfftw3f.so
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
    # Holo: upstream has libspandsp.so, but we don't have a new enough spandsp in base yet
    spandsp
    systemd-libs
    webrtc-audio-processing-1 libwebrtc-audio-processing-1.so
  )
  provides=(
    ladspa-host
    lv2-host
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

  # directories for overrides
  mkdir -p "$pkgdir/etc/pipewire/jack.conf.d"

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 pipewire/COPYING

  # Holo: we symlink the jack.conf.d directory from /etc/pipewire to /run because at
  # runtime the script pipewire-hwconfig picks up the correct config files based
  # on the hw.
  mkdir -p "$pkgdir/etc/pipewire"
  ln -s /run/pipewire/jack.conf.d "$pkgdir"/etc/pipewire/jack.conf.d
}

package_pipewire-onnx() {
  pkgdesc+=" - ONNX filter support"
  depends=(
    "pipewire-audio=$epoch:$pkgver-$pkgrel"
    "pipewire=$epoch:$pkgver-$pkgrel"
    glibc
    onnxruntime
  )

  mv onnx/* "$pkgdir"

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

  # directory for overrides
  mkdir -p "$pkgdir/etc/pipewire/pipewire-pulse.conf.d"

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
