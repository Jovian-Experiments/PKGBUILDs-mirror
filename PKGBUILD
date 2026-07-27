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
pkgrel=1.11
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
    "0017-pulse-server-Expose-commands-for-sink-volume-control.patch"
    "0018-spa-varlink-Set-a-default-read-timeout-for-sync-call.patch"

    # Holo: include patch to emit a node error event when snd_pcm_start() fails
    # Note that this patch is too specific for the Deck and there is no upstream MR for it
    # See holo-team/tasks#1808
    "0001-alsa-emit-a-node-error-event-when-snd_pcm_start-fail.patch"

    # Holo: Backport https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2856
    "0001-alsa-acp-emit-route-param-updates-when-card-properti.patch"

    # Holo: Backport of https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2850
    "0001-spa-alsa-Detect-ports-for-HDMI-AC3-profiles.patch"
    "0002-alsa-fix-warning.patch"
    "0001-spa-alsa-Don-t-look-up-h-w-dev-index-for-DTS-AC3-dev.patch"

    # Holo: Backport of https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2882
    "0001-pulse-server-don-t-consider-monitor-nodes-when-findi.patch"

    # Holo: Backport of https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2873
    "0001-pipewire-pulse-Expose-profile-preference-setting-as-.patch"

    # Holo: Backport of https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2922
    "0001-spa-alsa-recheck-ACP-profile-set-on-HDMI-ELD-changes.patch"

    # Holo: Backport of https://gitlab.freedesktop.org/pipewire/pipewire/-/merge_requests/2994
    "0001-spa-alsa-pass-ELD-data-to-ACP-HDMI-profile-recheck.patch")
b2sums=('054c756beae00a1dc9b757864633f9698a8f6cf5c7c187b2f0d0cb762eec74990e3403e949684b24a5e67d499c9257a91fbd7ebbe764ee34fd02f92844419427'
        'b999796fc69ecd661b7cd761b98daf81412e4a02e649d74d8d8ec7d2c6cf0169f6062ea03131313a5b03a50529e956289baf0068f0631ea58243d42f1fae4d6e'
        'ba33b056d13739e24b7e6c46bf9268357eea5a989f8af5021c737978a9a0bd9fb9882cc7e2c6eb8477d7c1e50684c3083ea33123f29a949e600ee1849cfe5cdf'
        '2708c004cbfccc56b6342785f117f2f2ec16aba474df96acf4c9d028462b4c0b8f443f13f387465e24eb628f797615c58e91b53672e01729d18b46da72686d93'
        '23b4ff805917e71741672b5fd2efcccbd9ba65504f3ed776960c70742a29ee8b1c2ec0ba8c068792b949e58da59cc9978ad5b02fe9aa7f6074848c765cc8e906'
        '5e858d87ffc697bea4ab86c2d11b9802e0919c61a43863aeab2077c1d26e7907064f1d5ef24203aba9fb22c36ca1d828e64636e2e448b2df2abc5f78199d3a58'
        '433ecedab74b2db00d366f47f157874725462a6335cd5786fb66fbcfff98ff1aea63043b1d25299ab575db11582592d4c1bce3dddd0f206a68b340a90c90dfeb'
        'e4d9cc9b1ed543716bdedab2e9062de93cc18e6ceb829dca830859cea39df5de04598a4912f693d48bae780892dc2bf0ab34fb2b43f4b8e343eb9ad69dae79fe'
        'c8e88a1486d866ca73b46169d6875309295563b7969b9f6b38c212b81327a4dddb017858a79be99e0d6c28b23012c92c92f14705a82860a1435da2c0d17b6e91'
        '8d6e858b32c4664ec62873a59222b4364c1bfb600e17d7100bda1dc9376630e1765770f7acbe4dc689884b1712c8fe00d4a09ac067ea90a854baf3a0d60d2324'
        '86e618a9a2406e0e46707d5661580f6df2c1beffa905e160a1c3734becdba72c37430f48a8900b6a1d3a8dc0af98f8713db8eed874da8b93c779b461e7e3dbfb'
        'eaab5aa942ec188f2c4a3cf191a38b1d6e313501e422c906cd8b5e2253b187eced8c2882016cae23e78d7cb011cca0a473d6dbf957ef0b1f9c32b5a8e0a74f39'
        '8f3f78063fde7d3cc0d14e164e08811f384f226b6fd30a80590ed7830fc49509bea4bfa6d439d03db547d5499a9b01e629eacc22a884b984cfc4d0e64f6d5189'
        '0ccbf2aec38873219c43e5385ded7ea625d689326eede025620cbdbda27da495372b884cf450ca951d7a6db210f5bd9afca5ddbd20929f0edb4ea7d20f65a7b5'
        'ef4e383e318ac1f42b2b31b564962d3bcd9d6a7d55366f713e466dfbb3f25f93a15ee6a4217ae7fb6f4c06017041d58ef9acca45232f8a878c6388caf2a322dd'
        '394ac5084dcac5cb216ad3ea3fb6a4dd2ad1f4a78b03c5671220619cfa6e6944c45d78dedfa83eaa7c5fdb8c28f009525b16d25d8a8fb6558f4b9802871650cd'
        '738ccabfecb709593a900705897c7a21da76adbbfbcd7615797f87d20ab4c700fc4097977e55b3fb8139927132fdc2a9da6ae6d071241b3e3f2c4ea2349546c9'
        'd050df52be8b8467b1a64dc3f76ef5151f9667dd3fb0776ca03ff3c5116dba36f728edb8475ccbd6b8944db415f258cb8e60c009e7ceb26cbe751fac56eccecd'
        '55ac6dda66c7006548a4ac4a1e49a77f38817e7e873ddf8d5bc2efa448582362782630621a8b509f48a4cdc6581aa7a9327a719853ca80f29e6a0ebbe911bacd'
        '86ef3c1b02272b5b2936fa34fb082dd1d8242e299057af7216c10054eb8254c23d29c84a95763385e59507ff9853aeb1eda78be995763b9ae79b1f62c7ac0e52'
        '8f1cb3be599496ab2bc898a6ebbdaf131f286644ad23f57f76d79884d9d2b7757c7247a84e964abffb259721c87474b058a38df118ecb69a4542870caebe94f8'
        '46656b0301e0a8516762f4f7d6933e642fa4ab83d4e3b6bbf1d7bfa9c1a54e6c679724f092b8ef32f28e410cb593a0917318c061eebecad48c91a6ca1a25df6a'
        '585b5f0dcd6f04f890cad851aa3bb462125db4219da2da1a3edf0e63706be11542ca72dff0d357838e5f02ce247014e7e1b4be8f1feef2cc8f4b22200723a750'
        '3d3664007c21b4c9d2c555bda8d9c8b8695baf9bdf2946f5583905ac5e9420fb60b9e82bf4e68175752032d3de0ca13e71c4e1ab139cb648c2d62b5e3430b3c9'
        'c0b40436099a3278c97cd96fdc007a5dd9a28eb692e494baba3e09cf428ffe4c96e087d77fcb12b3b24994933028aa4eb21618da90c424346d752f53ce5c9d61'
        '36f4bb59374e85fcb1a4b4281b027a54e7262476657735a3db0b3b8ef93bd4ca3cf9a2f7909f5deff527cdb6628c0ae7125815e1261f048db1282b99d0a97ad4'
        '0c07c7488e6463d83ed2c0e89df4ad8e2e10c5fcdfb1b66610aaf26672a08204d313d6cced8c4ebd2152b9f0211358b8ec3db42e1674355d32808de9a85b5b10'
        'ac9cadb5252779f86825b778e7c79ea7e926b1ebaba0b9fc504167b6d944b6fe33f4b4833ecf5751b4723592749dd1c856a419426dde864b620b08cb23a38ba7'
        '8dc405657ce215407e7189c4c35e38618568763b07aea30ce805da38cd593943e434fcf55fb6a77f172408f99ac6fb701eefdf0da8d7c30f280e9b79163e3e2c'
        'adc941999ee419b3f25bf155cf59e29344a32ea94067ec1530c1b069912eb825fdc908c72a89ef536df50293b1807f403a8560319a366838a4a55ed6ead8e852'
        '43c150e442e62b1c5da74572aa280804c06e60323e527404a3369310186fd3a230d0248c90c1e008b0cfa313f260876ecaf08a4a6dd6f82a4db1ddefaa06984c'
        '1b2f8b5c201706c2faaedb95de487d1af70394f8f446819d82fc7163d142010bb3b212457a7b5c02bc4e3605d7a5e2be3fcb562cfb80ff551998343264160a6b')

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
    # Holo: don't create the libraries since we symlink to /run/...
    #mkdir -p etc/pipewire/{client-rt,client,minimal,pipewire}.conf.d

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
  # Holo: don't create the libraries since we symlink to /run/...
  #mkdir -p "$pkgdir/etc/pipewire/jack.conf.d"

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
  # Holo: don't create the libraries since we symlink to /run/...
  #mkdir -p "$pkgdir/etc/pipewire/pipewire-pulse.conf.d"

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
