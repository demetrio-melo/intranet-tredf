import AreaView from './components/Views/AreaView';
import PessoaView from './components/Views/PessoaView';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';
  config.settings.image_crop_aspect_ratios = [
    {
      label: '16:9',
      ratio: 16 / 9,
    },
    {
      label: '4:3',
      ratio: 4 / 3,
    },
    {
      label: '1:1',
      ratio: 1,
    },
  ];
  // Registra Visoes padrao para tipos de conteúdo
  config.views.contentTypesViews = {
    Area: AreaView,
    Pessoa: PessoaView,
    ...config.views.contentTypesViews,
  };
  return config;
};

export default applyConfig;
