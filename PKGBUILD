# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=mesa-unstable
# Jupiter: drop radv vulkan driver - separate sources and package
pkgname=('vulkan-mesa-layers-unstable' 'opencl-mesa-unstable' 'vulkan-intel-unstable' 'vulkan-swrast-unstable' 'libva-mesa-driver-unstable' 'mesa-vdpau-unstable' 'mesa-unstable')
pkgdesc="An open-source implementation of the OpenGL specification"
_tag=radeonsi-3.5.0
pkgver=23.1.2.170169.radeonsi_3.5.0
pkgrel=1.1
arch=('x86_64')
makedepends=('git' 'openssh' 'python-mako' 'libxml2' 'libx11' 'xorgproto' 'libdrm' 'libxshmfence' 'libxxf86vm'
             'libxdamage' 'libvdpau' 'libva' 'wayland' 'wayland-protocols' 'zstd' 'elfutils' 'llvm'
             'libomxil-bellagio' 'libclc' 'clang' 'libglvnd' 'libunwind' 'lm_sensors' 'libxrandr'
             'systemd' 'valgrind' 'glslang' 'vulkan-icd-loader' 'directx-headers' 'cmake' 'meson')
url="https://www.mesa3d.org/"
license=('custom')
options=('debug' '!lto')
source=("jupiter-mesa::git+ssh://git@gitlab.steamos.cloud/jupiter/mesa.git#tag=$_tag"
        LICENSE)
sha512sums=('SKIP'
            'f9f0d0ccf166fe6cb684478b6f1e1ab1f2850431c06aa041738563eb1808a004e52cdec823c103c9e180f03ffc083e95974d291353f0220fe52ae6d4897fecc7')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D'  # Emil Velikov <emil.l.velikov@gmail.com>
              '946D09B5E4C9845E63075FF1D961C596A7203456'  # Andres Gomez <tanty@igalia.com>
              'E3E8F480C52ADD73B278EE78E1ECBE07D7D70895'  # Juan Antonio Suárez Romero (Igalia, S.L.) <jasuarez@igalia.com>
              'A5CC9FEC93F2F837CB044912336909B6B25FADFA'  # Juan A. Suarez Romero <jasuarez@igalia.com>
              '71C4B75620BC75708B4BDB254C95FAAB3EB073EC'  # Dylan Baker <dylan@pnwbakers.com>
              '57551DE15B968F6341C248F68D8E31AFC32428A6') # Eric Engestrom <eric@engestrom.ch>

pkgver() {
  cd jupiter-mesa

  _ver=$(cat VERSION)
  #echo ${_ver/-/_}.$(git rev-list --count HEAD).$(git rev-parse --short HEAD)
  echo "${_ver/-/_}.$(git rev-list --count HEAD).${_tag//-/_}"
}

build() {
  # Build only minimal debug info to reduce size
  CFLAGS+=' -g1'
  CXXFLAGS+=' -g1'

  # Jupiter:
  #  - drop most gallium drivers but radeonsi, swrast and zink
  #  - drop radv vulkan driver - separate sources and package
  #  - disable xa - unused by our gallium drivers
  arch-meson jupiter-mesa build \
    --prefix=/usr/lib/steamos/mesa \
    -D b_ndebug=true \
    -D b_lto=false \
    -D platforms=x11,wayland \
    -D gallium-drivers=radeonsi,swrast,zink \
    -D vulkan-drivers=intel,swrast \
    -D vulkan-layers=device-select,intel-nullhw,overlay \
    -D dri3=enabled \
    -D egl=enabled \
    -D gallium-extra-hud=true \
    -D gallium-nine=true \
    -D gallium-omx=bellagio \
    -D gallium-opencl=icd \
    -D gallium-va=enabled \
    -D gallium-vdpau=enabled \
    -D gallium-xa=disabled \
    -D android-libbacktrace=disabled \
    -D gbm=enabled \
    -D gles1=disabled \
    -D gles2=enabled \
    -D glvnd=true \
    -D glx=dri \
    -D libunwind=enabled \
    -D llvm=enabled \
    -D lmsensors=enabled \
    -D osmesa=true \
    -D shared-glapi=enabled \
    -D microsoft-clc=disabled \
    -D video-codecs=vc1dec,h264dec,h264enc,h265dec,h265enc \
    -D valgrind=enabled

  # Print config
  meson configure build

  ninja -C build
  meson compile -C build

  # fake installation to be seperated into packages
  # outside of fakeroot but mesa doesn't need to chown/mod
  DESTDIR="${srcdir}/fakeinstall" meson install -C build
}

_install() {
  local src f dir
  for src; do
    f="${src#fakeinstall/}"
    dir="${pkgdir}/${f%/*}"
    install -m755 -d "${dir}"
    mv -v "${src}" "${dir}/"
  done
}

package_vulkan-mesa-layers-unstable() {
  pkgdesc="Mesa's Vulkan layers"
  depends=('libdrm' 'libxcb' 'wayland' 'python>=3.11' 'python<3.12')
  conflicts=('vulkan-mesa-layer')
  replaces=('vulkan-mesa-layer')

  _install fakeinstall/usr/lib/steamos/mesa/share/vulkan/explicit_layer.d
  _install fakeinstall/usr/lib/steamos/mesa/share/vulkan/implicit_layer.d
  _install fakeinstall/usr/lib/steamos/mesa/lib/libVkLayer_*.so
  _install fakeinstall/usr/lib/steamos/mesa/bin/mesa-overlay-control.py

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_opencl-mesa-unstable() {
  pkgdesc="OpenCL support for AMD/ATI Radeon mesa drivers"
  # Jupiter: clang-libs is a local thing, which we should upstream in Arch
  depends=('libdrm' 'libclc' 'clang-libs' 'expat')
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  provides=('opencl-driver')

  _install fakeinstall/usr/lib/steamos/mesa/etc/OpenCL
  _install fakeinstall/usr/lib/steamos/mesa/lib/lib*OpenCL*
  _install fakeinstall/usr/lib/steamos/mesa/lib/gallium-pipe

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_vulkan-intel-unstable() {
  pkgdesc="Intel's Vulkan mesa driver"
  depends=('wayland' 'libx11' 'libxshmfence' 'libdrm' 'zstd' 'systemd-libs')
  optdepends=('vulkan-mesa-layers: additional vulkan layers')
  provides=('vulkan-driver')

  _install fakeinstall/usr/lib/steamos/mesa/share/vulkan/icd.d/intel_icd*.json
  _install fakeinstall/usr/lib/steamos/mesa/lib/libvulkan_intel.so

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_vulkan-radeon-unstable() {
  pkgdesc="Radeon's Vulkan mesa driver"
  depends=('wayland' 'libx11' 'libxshmfence' 'libelf' 'libdrm' 'llvm-libs' 'systemd-libs')
  optdepends=('vulkan-mesa-layers: additional vulkan layers')
  provides=('vulkan-driver')

  _install fakeinstall/usr/lib/steamos/mesa/share/vulkan/icd.d/radeon_icd*.json
  _install fakeinstall/usr/lib/steamos/mesa/libvulkan_radeon.so

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_vulkan-swrast-unstable() {
  pkgdesc="Vulkan software rasteriser driver"
  depends=('wayland' 'libx11' 'libxshmfence' 'libdrm' 'zstd' 'llvm-libs' 'systemd-libs' 'libunwind')
  optdepends=('vulkan-mesa-layers: additional vulkan layers')
  conflicts=('vulkan-mesa')
  replaces=('vulkan-mesa')
  provides=('vulkan-driver')

  _install fakeinstall/usr/lib/steamos/mesa/share/vulkan/icd.d/lvp_icd*.json
  _install fakeinstall/usr/lib/steamos/mesa/lib/libvulkan_lvp.so

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_libva-mesa-driver-unstable() {
  pkgdesc="VA-API implementation for gallium"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'libelf' 'libxshmfence')
  depends+=('libexpat.so')

  _install fakeinstall/usr/lib/steamos/mesa/lib/dri/*_drv_video.so

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_mesa-vdpau-unstable() {
  pkgdesc="Mesa VDPAU drivers"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'libelf' 'libxshmfence')
  depends+=('libexpat.so')

  _install fakeinstall/usr/lib/steamos/mesa/lib/vdpau

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}

package_mesa-unstable() {
  depends=('libdrm' 'wayland' 'libxxf86vm' 'libxdamage' 'libxshmfence' 'libelf'
           'libomxil-bellagio' 'libunwind' 'llvm-libs' 'lm_sensors' 'libglvnd'
           'zstd' 'vulkan-icd-loader')
  depends+=('libsensors.so' 'libexpat.so' 'libvulkan.so')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'mesa-vdpau: for accelerated video playback'
              'libva-mesa-driver: for accelerated video playback')

  _install fakeinstall/usr/lib/steamos/mesa/share/drirc.d/00-mesa-defaults.conf
  _install fakeinstall/usr/lib/steamos/mesa/share/glvnd/egl_vendor.d/50_mesa.json

  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast, swr
  _install fakeinstall/usr/lib/steamos/mesa/lib/dri/*_dri.so

  _install fakeinstall/usr/lib/steamos/mesa/lib/bellagio
  _install fakeinstall/usr/lib/steamos/mesa/lib/d3d
  _install fakeinstall/usr/lib/steamos/mesa/lib/lib{gbm,glapi}.so*
  _install fakeinstall/usr/lib/steamos/mesa/lib/libOSMesa.so*
  # Jupiter: we don't build xa
  #_install fakeinstall/usr/lib/steamos/mesa/lib/libxatracker.so*

  _install fakeinstall/usr/lib/steamos/mesa/include
  _install fakeinstall/usr/lib/steamos/mesa/lib/pkgconfig

  # libglvnd support
  _install fakeinstall/usr/lib/steamos/mesa/lib/libGLX_mesa.so*
  _install fakeinstall/usr/lib/steamos/mesa/lib/libEGL_mesa.so*

  # indirect rendering
  ln -s /usr/lib/libGLX_mesa.so.0 "${pkgdir}/usr/lib/steamos/mesa/lib/libGLX_indirect.so.0"

  # make sure there are no files left to install
  find fakeinstall -depth -print0 | xargs -0 rmdir

  install -m644 -Dt "${pkgdir}/usr/lib/steamos/mesa/share/licenses/${pkgname}" LICENSE
}
